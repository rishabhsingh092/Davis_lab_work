# Question 6: Find Maximum and Minimum in Tuple
# Problem Statement:
# Find the maximum and minimum elements in a tuple without using built-in functions


tup = (5, 1, 8, 3)

max_val = tup[0]
min_val = tup[0]

for num in tup:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max =", max_val, "Min =", min_val)