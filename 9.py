for a in range(0, 334):
    for b in range(a + 1, 1001):
        c = 1000 - b - a
        if c <= b:
            break
        if a * a + b * b == c * c:
            print(a * b * c)