import sys
input = sys.stdin.readline


# def nextPermutation(list_a):

# 	k = -1
# 	m = -1

# 	for i in range(len(list_a)-1):
# 		if list_a[i] < list_a[i+1]:
# 			k = i
# 	if k == -1:
# 		return [-1]
# 	for i in range(k,len(list_a)):
# 		if list_a[k] < list_a[i]:
# 			m = i
# 	list_a[k],list_a[m] = list_a[m],list_a[k]
# 	list_a = list_a[:k+1] + sorted(list_a[k+1:])

# 	return list_a


# while True:
# 	i = list(map(int,input().split()))


# 	arr = i[1:]
# 	if i[0] == 0:
# 		break
# 	while True:
# 		if nextPermutation(arr) == [-1]:
# 			break
# 		else:
# 			print(nextPermutation(arr))

def dfs(depth,idx):
	# print(arr)
	if depth == 6:
		print(*list,sep=' ')
		return
	else:
		for i in arr:
			if not visited[i] and (depth ==0 or int(list[-1]) < i ):
				if depth > 0:
					print(int(list[-1]))
					print(i)
				visited[i] = 1
				dfs(depth+1,list+str(i),arr)
				list = list[:depth]
				visited[i] = 0


# def dfs(depth,list,arr):
# 	if depth == 6:
# 		print(*list,sep=' ')
# 		return
# 	else:
# 		for i in range(1,len(arr)+1):
# 			if not visited[i] and (depth ==0 or int(list[-1]) < arr[i-1]):
# 				visited[i] = 1
# 				dfs(depth+1,list+str(arr[i-1]),arr)
# 				visited[i] = 0

def dfs(depth,idx):
	if depth == 6:
		print(*answer)
		return
	for i in range(idx,end):
		answer.append(arr[i])
		dfs(depth+1,i+1)
		answer.pop()

while True:
	i = list(map(int,input().split()))
	end = i[0]
	arr = i[1:]
	answer = []
	if end == 0:
		break
	dfs(0,0)
	print()

