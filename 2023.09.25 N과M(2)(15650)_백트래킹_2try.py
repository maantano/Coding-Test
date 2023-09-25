N, M = map(int,input().split())
check_list = [0] * (N+1)
answer_list = []

def dfs(n, small_list):
    if n == M:
        answer_list.append(small_list)
        return
    for i in range(1,N+1):
        if small_list[-1] > i:
            continue
        if check_list[i] == 0:
            check_list[i] = 1
            dfs(n+1,small_list+[i])
        check_list[i] = 0

dfs(0, [0])
for i in answer_list:
    i.pop(0)
    print(*i)



from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product

arr = list(i for i in range(1,N+1))
arr2 = list(i for i in range(1,N+1))

for i in product(arr,arr2,repeat=1):
	print(*i)
