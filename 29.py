Set = set()
for i in range(2, 101):
    for j in range(2, 101):
        Set.add(pow(i, j))
print(len(Set))