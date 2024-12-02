import numpy as np
import os

data_path = os.path.join(os.getcwd(), "data.txt")
reports_np = np.loadtxt(data_path, dtype=(int, int), )

print(reports_np)
