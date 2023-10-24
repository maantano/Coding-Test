# 6
# 9
# 2 7 4 1 5 3
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int,input().split()))

arr.sort()

p1 = 0
p2 = n-1
cnt = 0
while p1 < p2:
	if arr[p1] + arr[p2] == m:
		cnt+=1
		p1+=1
		p2-=1
	elif arr[p1] + arr[p2] < m:
		p1+=1
	else:
		p2-=1
print(cnt)
