# Question 9: Merge and Sort Unique Elements
# Problem Statement:
# Merge two lists and return a sorted list of unique elements.


l1 = [3, 1, 2]
l2 = [2, 4, 5]

merged = list(set(l1 + l2))
merged.sort()

print(merged)