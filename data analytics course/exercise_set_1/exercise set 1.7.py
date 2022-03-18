import numpy as np

list1 = np.arange(1, 50).reshape(7, 7)
list1[:] = list1 + 50
summed = np.sum(list1)
odd = list1[list1 % 2 != 0]
summed_odd = np.sum(odd)
deviation = np.std(list1)
summed_row = np.sum(list1, axis=1)
summed_column = np.sum(list1, axis=0)