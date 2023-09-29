# import sys
# n = int(sys.stdin.readline().rstrip())
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0
for i in range(1,n):
	post = arr[:i]
	behind = arr[i:]
	print('post ==>',post ,'==== behind ===>',behind)
# arr = []
# arr.append(int(sys.stdin.readline().split()))
# for i in range(n):

print(arr)
