import numpy as np

# Number of Type A and Type B servers
# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory

A = np.array([
    [4, 2],
    [8, 12]
])

b = np.array([24, 72])

solution = np.linalg.solve(A, b)

print("Type A servers:", solution[0])
print("Type B servers:", solution[1])

print("Verification:", A @ solution)

# Real-world example: Hospital equipment allocation

import numpy as np

# Type A equipment uses 5 power units and 10 GB storage
# Type B equipment uses 3 power units and 5 GB storage

A = np.array([
    [5, 3],
    [10, 5]
])

b = np.array([21, 35])

solution = np.linalg.solve(A, b)

print("\nHospital Equipment Allocation")
print("Type A equipment:", solution[0])
print("Type B equipment:", solution[1])

print("Verification:", A @ solution)