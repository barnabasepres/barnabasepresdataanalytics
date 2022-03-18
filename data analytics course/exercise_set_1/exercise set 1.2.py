import numpy as np

list1 = np.zeros(5)

list2 = np.ones(15)

list3 = np.ones(15) * 7

list4 = np.arange(100, 151)

list5 = np.arange(1900, 2022)

list6 = np.arange(0, 101)
list6_mod = list6[list6 % 2 == 0]

list7 = np.arange(1950, 2021)
list8_mod = list7[list7 % 4 ==0]