import numpy as np
import os

data_path = os.path.join(os.getcwd(), "data.txt")
data_file = open(data_path, "r")
word_search_str = data_file.read()


def get_top_left_to_bottom_right_diagonals(matrix):
    rows, cols = matrix.shape
    diagonals = []

    for offset in range(-rows + 1, cols):
        diagonals.append(matrix.diagonal(offset))

    return diagonals


lines = word_search_str.split("\n")[:-1]
lines_arr = np.array(lines)
word_search_matrix = np.array([list(line) for line in lines])
lines_inverted_arr = np.apply_along_axis("".join, axis=0, arr=word_search_matrix)
diagonals = get_top_left_to_bottom_right_diagonals(word_search_matrix)
principal_diagonals_str_arr = np.array(["".join(diagonal) for diagonal in diagonals])
second_diagonals = get_top_left_to_bottom_right_diagonals(np.rot90(word_search_matrix))
second_diagonals_str_arr = np.array(
    ["".join(diagonal) for diagonal in second_diagonals]
)


horizontal_founds = np.strings.count(lines_arr, "XMAS")
horizontal_founds_total = np.sum(horizontal_founds)
horizontal_inverted_founds = np.strings.count(lines_arr, "SAMX")
horizontal_inverted_founds_total = np.sum(horizontal_inverted_founds)

vertical_founds = np.strings.count(lines_inverted_arr, "XMAS")
vertical_founds_total = np.sum(vertical_founds)
vertical_inverted_founds = np.strings.count(lines_inverted_arr, "SAMX")
vertical_inverted_founds_total = np.sum(vertical_inverted_founds)


principal_diagonals_founds = np.strings.count(principal_diagonals_str_arr, "XMAS")
principal_diagonals_founds_total = np.sum(principal_diagonals_founds)
principal_diagonals_inverted_founds = np.strings.count(
    principal_diagonals_str_arr, "SAMX"
)
principal_diagonals_inverted_found_total = np.sum(principal_diagonals_inverted_founds)

second_diagonals_founds = np.strings.count(second_diagonals_str_arr, "XMAS")
second_diagonals_found_total = np.sum(second_diagonals_founds)
second_diagonals_inverted_founds = np.strings.count(second_diagonals_str_arr, "SAMX")
second_diagonals_inverted_found_total = np.sum(second_diagonals_inverted_founds)


total_founds = (
    horizontal_founds_total
    + horizontal_inverted_founds_total
    + vertical_founds_total
    + vertical_inverted_founds_total
    + principal_diagonals_founds_total
    + principal_diagonals_inverted_found_total
    + second_diagonals_found_total
    + second_diagonals_inverted_found_total
)


print(total_founds)
