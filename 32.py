num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vis = [True] * 10
ans_set = set()

global ans
ans = 0

def Check(num1, num2):
    if num1 * num2 in ans_set:
        return False
    num = num1 * num2
    num_list = []
    while num1:
        num_list.append(num1 % 10)
        num1 = int(num1 / 10)
    while num2:
        num_list.append(num2 % 10)
        num2 = int(num2 / 10)
    while num:
        num_list.append(num % 10)
        num = int(num / 10)
    if len(num_list) == 9:
        num_list.sort()
        for i in range(9):
            if num_list[i] != i + 1:
                return False
        return True
    else:
        return False

def Find_Pandigital(num1, num2):
    if num1 > 10000:
        return
    if num1 < num2:
        return
    if num1 != 0 and num2 != 0:
        global ans
        if Check(num1, num2):
            ans_set.add(num1 * num2)
            ans += num1 * num2
            print(num1, num2, num1 * num2)
    if num2 != 0:
        for i in num:
            if vis[i] == True:
                vis[i] = False
                Find_Pandigital(num1, num2 * 10 + i)
                vis[i] = True
    else:
        for i in num:
            if vis[i] == True:
                vis[i] = False
                Find_Pandigital(num1 * 10 + i, num2)
                vis[i] = True
        for i in num:
            if vis[i] == True:
                vis[i] = False
                Find_Pandigital(num1, num2 * 10 + i)
                vis[i] = True

Find_Pandigital(0, 0)
print(ans)