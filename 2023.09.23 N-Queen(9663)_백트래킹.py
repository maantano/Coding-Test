N = int(input())




stack = []

def backT(x,y):
	arr = [[0]*N for _ in range(N)]
	arr[x][y] = 1
	if x >= N or y >= N:
		return
	for i in range(N-2):
		if arr[x][i] == 1:
			stack.append((x,i))
			if x >= N or y >= N:
				continue
			backT(x+1,y+2)

backT(0,0)
print('stack ===>',len(stack))
