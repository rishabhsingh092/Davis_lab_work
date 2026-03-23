# Question 2: List Rotation
# Problem Statement:
# Rotate a list to the right by k positions.



lst = [10, 20, 30, 40, 50]
k = 2

k = k % len(lst)  # handle large k
rotated = lst[-k:] + lst[:-k]

print(rotated)