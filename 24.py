global cnt
cnt = 0
List = [0] * 10
vis = [True] * 10

def Permutation(step):
    global cnt
    if step == len(List):
        cnt += 1
        if cnt == 1000000:
            for i in List:
                print(i, end = '')
            return 1
        return 0
    for i in range(0, len(List)):
        if vis[i] == True:
            List[step] = i
            vis[i] = False
            if Permutation(step + 1) == 1:
                return 1            
            vis[i] = True
    return 0

Permutation(0)