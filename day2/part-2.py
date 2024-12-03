import pandas as pd
import os

data_path = os.path.join(os.getcwd(), "data.txt")
reports_df = pd.read_csv(data_path, header=None, sep=" ", names=range(0, 8))


def verify_levels_safety(levels):
    levels_asc = levels.sort_values(ascending=True)
    levels_desc = levels.sort_values(ascending=False)

    if not levels.equals(levels_asc) and not levels.equals(levels_desc):
        return False

    safe = True

    for index in range(levels.shape[0]):
        if index == 0:
            continue

        diff = abs(levels.iloc[index - 1] - levels.iloc[index])

        if diff == 0 or diff > 3:
            safe = False
            break

    return safe


def verify_report_safety(levels):
    row_no_nan = levels.dropna()
    safe = verify_levels_safety(row_no_nan)

    if safe:
        return True

    safe_single_bad = False

    for index_to_delete in range(row_no_nan.shape[0]):
        levels_copy = row_no_nan.copy()
        levels_single_bad = levels_copy.drop(levels_copy.iloc[[index_to_delete]].index)
        safe_single_bad = verify_levels_safety(levels_single_bad)

        if safe_single_bad:
            break

    return safe_single_bad


is_safe_df = reports_df.apply(verify_report_safety, axis=1)
safe_reports_num = is_safe_df.sum()
print(safe_reports_num)
