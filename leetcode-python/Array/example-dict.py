d = dict()
nums = [1, 5, 3, 2, 9, 2, 3]
for i in nums:
    d[i] = d.get(i, 0) + 1

print(d)