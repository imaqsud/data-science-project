import numpy as np

# Change False to True to see Numpy arrays in action
if True:
    array = np.array([1, 4, 5, 8], float)
    print(array)
    print("")
    array = np.array([[1, 2, 3], [4, 5, 6]], float)  # a 2D array/Matrix
    print(array)

# Change False to True to see array indexing and slicing in action
if True:
    array = np.array([1, 4, 5, 8], float)
    print(array)
    print("")
    print(array[1])
    print("")
    print(array[:2])
    print("")
    array[1] = 5.0
    print(array[1])

# Change False to True to see Matrix indexing and slicing in action
if True:
    two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)
    print(two_D_array)
    print("")
    print(two_D_array[1][1])
    print("")
    print(two_D_array[1, :])
    print("")
    print(two_D_array[:, 2])

# Change False to True to see Array arithmetics in action
if True:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([5, 2, 6], float)
    print(array_1 + array_2)
    print("")
    print(array_1 - array_2)
    print("")
    print(array_1 * array_2)

# Change False to True to see Matrix arithmetics in action
if True:
    array_1 = np.array([[1, 2], [3, 4]], float)
    array_2 = np.array([[5, 6], [7, 8]], float)
    print(array_1 + array_2)
    print("")
    print(array_1 - array_2)
    print("")
    print(array_1 * array_2)

if True:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([[6], [7], [8]], float)
    print(np.mean(array_1))
    print(np.mean(array_2))
    print("")
    print(np.dot(array_1, array_2))
