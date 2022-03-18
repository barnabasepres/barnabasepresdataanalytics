import numpy as np

list1 = [23, 34, 54, 34, 56, 33, 56,
         78, 65, 78, 42, 32, 11, 34, 56]
array = np.array(list1).reshape(3, 5)


list2 = np.arange(128, 256).reshape(16, 8)

list3 = np.linspace(0.05, 5, 100).round(decimals=2).reshape(10, 10)
