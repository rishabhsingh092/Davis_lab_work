# Question 13: Flatten Nested List
# Problem Statement:
# Flatten a nested list (1 level deep).Question 13: Flatten Nested List
# Problem Statement:
# Flatten a nested list (1 level deep).


nested = [[1, 2], [3, 4], [5]]

flat = []

for sublist in nested:
    for num in sublist:
        flat.append(num)

print(flat)