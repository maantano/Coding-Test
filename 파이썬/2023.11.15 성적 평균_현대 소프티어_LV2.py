import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(k):
	a,b = map(int,input().split())
	print("{:.2f}".format((sum(arr[a-1:b]) / ((b-a)+1))))
