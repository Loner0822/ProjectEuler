cnt = 0
F1 = 0
F2 = 1

while True:
    cnt += 1
    tmp = F1 + F2
    F1 = F2
    F2 = tmp
    F1_str = str(F1)
    if len(F1_str) >= 1000:
        break
print(cnt)