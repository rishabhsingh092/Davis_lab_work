# Question 10: Tuple Pair Sum
# Problem Statement:
# Find all pairs in a tuple whose sum equals a given value.

tup = (1, 2, 3, 4, 5)
target = 5

pairs = []

for i in range(len(tup)):
    for j in range(i + 1, len(tup)):
        if tup[i] + tup[j] == target:
            pairs.append((tup[i], tup[j]))

print(pairs)