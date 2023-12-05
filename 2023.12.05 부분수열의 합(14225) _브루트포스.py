import sys
from itertools import combinations
input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))

# answer = {i:0 for i in range(1,100)}

# s = set()
# for i in range(1,n+1):
# 	for j in list(combinations(arr,i)):
# 		answer[sum(j)] +=1
# for i in range(1,10000001):
# 	if not answer[i]:
# 		print(i)
# 		break

n = int(input())
num = list(map(int,input().split()))
s = set()
for i in range(1,n+1):
	for j in combinations(num,i):
		s.add(sum(j))

ans = 1
for x in sorted(s):
	if x != ans:
		break
	ans+=1
print(ans)

# from itertools import combinations

# N, *A = map(int, open(0).read().split())
# res = set()
# for r in range(1, N + 1):
# 	for c in combinations(A, r):
# 		res.add(sum(c))

# ans = 1
# for x in sorted(res):
# 	if x != ans:
# 		break
# 	ans += 1
# print(ans)


# n = int(input())
# num = list(map(int,input().split()))
# visited = [0]*10000000

# def dfs(idx,sum) :
# 	if idx == n :
# 		return
# 	sum += num[idx]
# 	visited[sum] = 1
# 	dfs(idx+1, sum)
# 	dfs(idx+1, sum-num[idx])

# dfs(0,0)
# print(visited[1:].index(0)+1)





# # def dfs(idx,l):
# # 	if idx == n+1:
# # 		return l
# # 	else:
# # 		l += list(combinations(arr,idx))
# # 		return dfs(idx+1,l)
# # combi = dfs(1,[])


# # answer = {i:0 for i in range(1,100001)}
# # for i in range(len(combi)):
# # 		answer[sum(combi[i])]+=1

# # for i in range(1,100001):
# # 	if not answer[i]:
# # 		print(i)
# # 		break
