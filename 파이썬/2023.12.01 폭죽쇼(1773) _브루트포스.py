import sys
input = sys.stdin.readline

n,c = map(int,input().split())
visited= [0] * (c+1)
for i in range(n):
	a = int(input())
	if a == 1:
		print(c)
		exit()
	for k in range(a,c+1,a):
		visited[k] = 1
print(sum(visited))



# arr = []
# visited = [0] * (c+1)
# for i in range(n):
# 	arr.append(int(input()))
# cnt = 0
# for i in range(1,c+1):
# 	for j in arr:
# 		if i % j == 0 and not visited[i]:
# 			# visited[i] = 1
# 			cnt+=1

# # print(sum(visited))

# print(cnt)


