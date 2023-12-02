import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n = int(input())
k = int(input())

arr= [input().rstrip() for _ in range(n)]
visited = [0] * (n+1)

s = set()
def dfs(idx,l):
	if idx == k:
		s.add((''.join(l)))
		return
	else:
		for i in range(len(arr)):
			if not visited[i]:
				visited[i] =1
				dfs(idx+1,l+[arr[i]])
				visited[i] = 0

dfs(0,[])
print(len(s))


from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = [input().rstrip() for _ in range(n)]

res = set()
for i in permutations(arr, k): res.add("".join(i))
print(len(res))
