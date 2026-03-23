# Question 1: Find Duplicate Elements in a List
# Problem Statement:
# Write a program to find all duplicate elements in a given list.

lst = [1, 2, 3, 2, 4, 5, 1]

seen = set()
duplicates = set()

for num in lst:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(list(duplicates))