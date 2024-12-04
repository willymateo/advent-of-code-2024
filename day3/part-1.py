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


valid_expressions = re.findall(r"mul\(\d+,\d+\)", corrupted_code)
valid_expressions_arr = np.array(valid_expressions)
vectorized_exec_mul = np.vectorize(exec_mul)
mul_res_arr = vectorized_exec_mul(valid_expressions_arr)

print(mul_res_arr.sum())
