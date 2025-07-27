import numpy as np

arr1 = np.array([1, 2, 3, 4])
print("1. Array:", arr1)

zeros = np.zeros(4)
print("2. Zeros:", zeros)

ones = np.ones(4)
print("3. Ones:", ones)

arange_arr = np.arange(5, 15)
print("4. Arange:", arange_arr)

linspace_arr = np.linspace(0, 1, 5)
print("5. Linspace:", linspace_arr)

identity = np.eye(3)
print("6. Identity Matrix:\n", identity)

reshaped = np.reshape(np.arange(6), (2, 3))
print("7. Reshaped:\n", reshaped)

flattened = reshaped.ravel()
print("8. Flattened:", flattened)

transposed = reshaped.T
print("9. Transposed:\n", transposed)

print("10. Shape of array:", reshaped.shape)

print("11. Size of array:", reshaped.size)

print("12. Max value:", arr1.max())

print("13. Min value:", arr1.min())

print("14. Sum of array:", arr1.sum())

random_arr = np.random.rand(3)
print("15. Random array:", random_arr)
