# Question 15: Tuple to Dictionary Mapping
# Problem Statement:
# Convert two tuples into a dictionary where one tuple contains keys and the other contains values.

keys = ('a', 'b', 'c')
values = (1, 2, 3)

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)