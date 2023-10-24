import sys
input = sys.stdin.readline
# n=int(input())
n = 9
arr= list(map(int,'5 12 7 10 9 1 2 3 11'.split(' ')))
# arr= list(map(int,input().split()))
# m = int(input())
arr.sort()
m = 13

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
