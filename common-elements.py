# Question 3: Remove Common Elements from Two Lists
# Problem Statement:
# Remove elements from the first list that are present in the second list.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]

result = []

for num in list1:
    if num not in list2:
        result.append(num)

print(result)