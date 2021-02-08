a = [16, 15, 12, 19, 22, 1233, 11, 11]
b = [11, 1233, 12, 52, 323]

c = []

for i in a:
    if i in b and i not in c:
        c.append(i)

print(sorted(c))
