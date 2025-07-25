import numpy as np

# Array Creation
a = np.array([1, 2, 3])
b = np.zeros((2, 3))
c = np.ones((3, 2))
d = np.full((2, 2), 7)
e = np.eye(3)
f = np.arange(0, 10, 2)
g = np.linspace(0, 1, 5)

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)
print("f =", f)
print("g =", g)

# Array operations
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

add = np.add(x, y)
sub = np.subtract(x, y)
mul = np.multiply(x, y)
div = np.divide(x, y)
dot = np.dot(x, y)

print("\nadd =", add)
print("sub =", sub)
print("mul =", mul)
print("div =", div)
print("dot =", dot)

# Array manipulation
arr = np.array([[1, 2, 3], [4, 5, 6]])

transposed = arr.T
reshaped = arr.reshape(3, 2)
flattened = arr.flatten()

print("\ntransposed =", transposed)
print("reshaped =", reshaped)
print("flattened =", flattened)

# Statistical operation
data = np.array([1, 2, 3, 4, 5])

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
sum_all = np.sum(data)
min_val = np.min(data)
max_val = np.max(data)

print("\nmean =", mean)
print("median =", median)
print("std_dev =", std_dev)
print("sum_all =", sum_all)
print("min_val =", min_val)
print("max_val =", max_val)

# Indexing & Slicing
arr = np.array([[10, 20, 30], [40, 50, 60]])

print("\narr[1][2] =", arr[1][2])
print("arr[0, 1] =", arr[0, 1])
print("arr[:, 1] =", arr[:, 1])
print("arr[1, :] =", arr[1, :])

# Random numbers
rand1 = np.random.rand(3)
rand2 = np.random.randint(1, 10, 5)

print("\nrand1 =", rand1)
print("rand2 =", rand2)
