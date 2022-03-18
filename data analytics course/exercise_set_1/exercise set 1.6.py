import numpy as np

list1 = np.arange(1, 37).reshape(6, 6)
slice1 = list1[3:6, 2:6]
slice2 = list1[0: 4, 3]
slice3 = list1[2, 0:6]
slice4 = list1[3:6, 0:6]