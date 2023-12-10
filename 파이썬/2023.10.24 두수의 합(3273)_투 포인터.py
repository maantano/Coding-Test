import sys
input = sys.stdin.readline
n=int(input())
arr= list(map(int,input().split()))
m = int(input())
arr.sort()

p1 = 0
p2 = n-1
cnt=0
tmpSum = arr[p1]+arr[p2]
while p1<p2:
	if arr[p1]+arr[p2] == m:
		cnt+=1
		p1+=1
	elif arr[p1] + arr[p2] < m:
		p1+=1
	else:
		p2-=1

print(cnt)
