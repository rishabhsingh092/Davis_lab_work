

# Question 4: Tuple Element Frequency
# Problem Statement:
# Count the frequency of each element in a tuple.


tup = (1, 2, 2, 3, 1, 4)

freq = {}

for num in tup:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)