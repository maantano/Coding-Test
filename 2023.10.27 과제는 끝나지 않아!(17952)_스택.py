import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
stack = []
tmp = 0

for i in range(n):
	if arr[i][0] == 0:
		if stack:
			a,b,c = stack.pop()
			if  c <= 1:
				tmp+=b
			else:
				stack.append([a,b,c-1])
	else:
		if arr[i][2] == 1:
			tmp+=arr[i][1]
		else:
			stack.append([arr[i][0],arr[i][1],arr[i][2]-1])
print(tmp)
