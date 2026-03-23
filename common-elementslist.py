# Question 12: Common Elements in Three Lists
# Problem Statement:
# Find common elements present in three lists.

l1 = [1, 2, 3]
l2 = [2, 3, 4]
l3 = [2, 5, 3]

result = list(set(l1) & set(l2) & set(l3))

print(result)