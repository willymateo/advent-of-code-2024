import pandas as pd
import os

data_path = os.path.join(os.getcwd(), "data.txt")
reports_df = pd.read_csv(data_path, header=None, sep=" ", names=range(0, 8))


def verify_report_safety(row):
    row_no_nan = row.dropna()
    row_asc = row_no_nan.sort_values(ascending=True)
    row_desc = row_no_nan.sort_values(ascending=False)

    if row_no_nan.equals(row_asc) or row_no_nan.equals(row_desc):
        level_is_safe = True

        for index in range(row_no_nan.shape[0]):
            if index == 0:
                continue

            diff = abs(row_no_nan.iloc[index - 1] - row_no_nan.iloc[index])

            if diff == 0 or diff > 3:
                level_is_safe = False
                break

        return level_is_safe

    return False


is_safe_df = reports_df.apply(verify_report_safety, axis=1)
safe_reports_num = is_safe_df.sum()
print(safe_reports_num)
