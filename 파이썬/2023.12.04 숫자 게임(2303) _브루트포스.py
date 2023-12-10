from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
	l = list(map(int,input().split()))
	arr.append(list(combinations(l,3)))
chk = 0
answer = 0
for i in range(n):
	for j in range(len(arr[i])):
		if chk <= sum(arr[i][j]) % 10:
			chk = sum(arr[i][j]) % 10
			answer = i
print(answer+1)

