import itertools


for i in range(1, 5):
    dig = []
    for j in range(1, i + 1):
        dig.append(j)
    pmt = list(itertools.permutations(dig, i))
    print(pmt)
