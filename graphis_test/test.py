l1 = list(range(10))
l2 = list(range(20))

l3 = []

for i in range(len(l2)):
    l3.append(int(i * len(l1) / len(l2)))

print(l3)
