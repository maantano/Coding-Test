import sys
input = sys.stdin.readline
import heapq
n,k = map(int,input().split())

# arr = [list(map(int,input().split())) for _ in range(n)]
q = {}
for i in range(n):
	ni,ki= map(int,input().split())
	q[ni] = ki
# q.sort(key=lambda x: x.keys())
arr = sorted(q.items() , key=lambda x : x[0])
# print(arr)
for i in arr:
	for j in
