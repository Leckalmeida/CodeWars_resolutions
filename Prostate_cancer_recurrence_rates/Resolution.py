def recurrence(values):
    nadir = min(values)
    idx_nadir = values.index(nadir)
    return any(value - nadir >= 2.0 - 1e-6 for value in values[idx_nadir + 1:])

# Test cases
input1 = [7.91, 2.43, 1.49, 0.99, 0.74, 0.48, 0.52, 0.50, 0.66, 1.26, 1.36, 1.35]
print(recurrence(input1))  # Output: False

input2 = [9.98, 8.56, 4.62, 1.16, 0.26, 0.37, 0.32, 1.02, 0.99, 1.56, 1.41, 2.35]
print(recurrence(input2))  # Output: True

input3 = [12.57, 6.86, 1.86, 1.93, 0.60, 1.46, 1.58, 1.58, 0.86, 0.72, 0.88, 2.1]
print(recurrence(input3))  # Output: False