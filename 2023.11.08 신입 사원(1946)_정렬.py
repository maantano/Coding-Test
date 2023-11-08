import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	arr = []
	answer = 1

	for i in range(n):
		arr.append(list(map(int,input().split())))

	arr.sort(key=lambda x : (x[0]))
	# print(arr)
	top = arr[0][1]
	for i in range(1,n):
		if arr[i][1] < top:
			top = arr[i][1]
			answer+=1
	print(answer)
