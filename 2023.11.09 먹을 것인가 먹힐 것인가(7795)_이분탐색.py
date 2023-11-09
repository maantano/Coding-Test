import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
	n,m = map(int,input().split())
	arr1 = sorted(list(map(int,input().split())))
	arr2 = sorted(list(map(int,input().split())))
	total = 0
	for i in arr2:
		start,end = 0,n-1
		while start <= end:
			mid = (start+end) // 2
			if arr1[mid] <= i:
				start = mid + 1
			else:
				end = mid -1
		total += (n-start)
	print(total)


