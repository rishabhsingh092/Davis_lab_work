# Question 11: Remove Empty Sets from List
# Problem Statement:
# Remove all empty sets from a list of sets.

lst = [{1, 2}, set(), {3, 4}, set()]

result = []

for s in lst:
    if s:  # empty set is False
        result.append(s)

print(result)