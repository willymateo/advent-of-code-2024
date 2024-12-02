import numpy as np
import os

data_path = os.path.join(os.getcwd(), "data.txt")
data_np = np.loadtxt(data_path, dtype=(int, int))
left_np = data_np[:, 0]
rigth_np = data_np[:, 1]


def calculate_total_distance(left, right):
    sorted_left = np.sort(left)
    sorted_rigth = np.sort(right)
    distance_difference = np.abs(sorted_left - sorted_rigth)

    return np.sum(distance_difference)


total_distance = calculate_total_distance(left=left_np, right=rigth_np)
print(total_distance)
