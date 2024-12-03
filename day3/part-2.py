import pandas as pd
import numpy as np
import os
import re

data_path = os.path.join(os.getcwd(), "data.txt")
data_file = open(data_path, "r")
corrupted_code = data_file.read()


def exec_mul(expression):
    numbers_list = re.findall(r"\d+", expression)
    numbers_arr = np.array(numbers_list, dtype=int)

    return np.prod(numbers_arr)


mul_expressions_iter = re.finditer(r"mul\(\d+,\d+\)", corrupted_code)
do_expressions_iter = re.finditer(r"do\(\)", corrupted_code)
dont_expressions_iter = re.finditer(r"don't\(\)", corrupted_code)
expressions_list = [
    (match.start(), match.end(), match.group()) for match in mul_expressions_iter
]
expressions_list.extend(
    [(match.start(), match.end(), match.group()) for match in do_expressions_iter]
)
expressions_list.extend(
    [(match.start(), match.end(), match.group()) for match in dont_expressions_iter]
)
expressions_df = pd.DataFrame(
    expressions_list, columns=["start_index", "end_index", "expression"]
).astype({"start_index": int, "end_index": int, "expression": str})
expressions_df = expressions_df.sort_values(by=["start_index"])


valid_mul_expressions_list = []
mul_expressions_are_enabled = True

for index, row in expressions_df.iterrows():
    if row.expression == "don't()":
        mul_expressions_are_enabled = False
    elif row.expression == "do()":
        mul_expressions_are_enabled = True
    elif mul_expressions_are_enabled:
        valid_mul_expressions_list.append(row.expression)


valid_mul_expressions_arr = np.array(valid_mul_expressions_list)
vectorized_exec_mul = np.vectorize(exec_mul)
mul_res_arr = vectorized_exec_mul(valid_mul_expressions_arr)

print(mul_res_arr.sum())
