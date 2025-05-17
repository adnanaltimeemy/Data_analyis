import numpy as np

# Task 1: Why doesn’t np.array((1, 0, 0), (0, 1, 0), (0, 0, 1), dtype=float)
# create a two-dimensional array? Write it the correct way.
# The code doesn't work because the np.array function needs a list or tuple of lists (or tuples) to create a 2D array.
# The correct way to create a 2D array is by passing a list of lists (or a tuple of tuples).

# Incorrect approach:
# np.array((1, 0, 0), (0, 1, 0), (0, 0, 1), dtype=float) # This causes a SyntaxError

# Correct approach:
matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)
print("Correct 2D Array:")
print(matrix)

# Task 2: Difference between np.array([0, 0, 0]) and np.array([[0, 0, 0]])
# np.array([0, 0, 0]) creates a 1D array with three elements.
# np.array([[0, 0, 0]]) creates a 2D array with one row and three columns.

a = np.array([0, 0, 0])  # 1D array
b = np.array([[0, 0, 0]])  # 2D array

print("\n1D Array:")
print(a)
print("Shape of 1D array:", a.shape)

print("\n2D Array:")
print(b)
print("Shape of 2D array:", b.shape)

# Task 3: Create a 3x4x4 array and slice it to obtain the specified values.
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)

# (a) 20.0
value_20 = arr[1, 1, 0]  # Accessing the value 20.0 in the array
print("\n20.0:", value_20)

# (b) [9. 10. 11. 12.]
row_2 = arr[1, 0, :]  # Extracting the second row from the second 2D slice
print("\n[9. 10. 11. 12.]:", row_2)

# (c) [[33. 34. 35. 36.]
#      [37. 38. 39. 40.]
#      [41. 42. 43. 44.]
#      [45. 46. 47. 48.]]
block = arr[2, :, :]  # Extracting the third 2D slice (index 2)
print("\n3x4 array block:")
print(block)

# (d) [[5. 6.], [21. 22.], [37. 38.]]
sliced_block = arr[:, 1:3, 0:2]  # Slicing from each 2D array
print("\n[[5. 6.], [21. 22.], [37. 38.]]:")
print(sliced_block)

# (e) [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
reverse_sliced_block = arr[2, :, 3:1:-1]  # Reverse slice along last axis
print("\n[[36. 35.] [40. 39.] [44. 43.] [48. 47.]]:")
print(reverse_sliced_block)

# (f) [[13. 9. 5. 1.]
#      [29. 25. 21. 17.]
#      [45. 41. 37. 33.]]
sliced_3d = arr[:, :, ::-4]  # Slicing every 4th element in reverse order along last axis
print("\n[[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]:")
print(sliced_3d)

# (g) [[1. 4.] [45. 48.]]
sliced_2d = arr[0:1, 0:2, ::3]  # Slicing 1st 2D array and picking every third element
print("\n[[1. 4.] [45. 48.]]:")
print(sliced_2d)

# (h) [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
sliced_rows = arr[1, :, :]  # Extracting the second slice and all columns
print("\n[[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]:")
print(sliced_rows)

# Conclusion: We have addressed all parts of the question with appropriate slicing techniques
