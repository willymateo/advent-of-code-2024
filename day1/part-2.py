import numpy as np
import os

data_path = os.path.join(os.getcwd(), "data.txt")
data_np = np.loadtxt(data_path, dtype=(int, int))
left_np = data_np[:, 0]
rigth_np = data_np[:, 1]


def calculate_total_similarity(left, right):
    left_occurences_in_rigth = [
        np.count_nonzero(item == right) for item in left
    ]

    similarities = left * left_occurences_in_rigth

    return np.sum(similarities)


total_similarity = calculate_total_similarity(left=left_np, right=rigth_np)
print(total_similarity)
