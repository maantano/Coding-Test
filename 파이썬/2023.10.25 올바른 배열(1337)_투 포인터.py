import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
tmp =[]

for i in range(0,n):
	cnt = 0
	for j in range(arr[i],arr[i]+5):
		if j not in arr:
			cnt+=1
	tmp.append(cnt)
print(min(tmp))
