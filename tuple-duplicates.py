# Question 5: Convert List to Tuple and Remove Duplicates
# Problem Statement:
# Convert a list into a tuple after removing duplicate elements.

lst = [1, 2, 2, 3, 4, 4]

unique = list(set(lst))
result = tuple(unique)

print(result)