import numpy as np

array = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("Array:")
print(array)

# This array is 1D with three elements
a = np.array([0, 0, 0])

# This array is 2D with one row and three columns
b = np.array([[0, 0, 0]])

# This array is 2D with three rows and one column
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)

print(arr[1, 0, 3])  

print(arr[0, 2, :])  

arrray3 = arr[2, :, :]
print(arrray3)

result4 = arr[:, 1, 0:2]
print(result4)

result5 = arr[2, :, 2:4][:, ::-1]
print(result5)

result6 = np.array([arr[0, :, 0][::-1], arr[1, :, 0][::-1], arr[2, :, 0][::-1]])
print(result6)

result7 = np.array([[arr[0, 0, 0], arr[0, 0, 3]],  # [1, 4]
                   [arr[2, 3, 0], arr[2, 3, 3]]])  # [45, 48]
print(result7)

result8 = np.array([arr[1, 2:, :], arr[2, :2, :]])
print(result8)

