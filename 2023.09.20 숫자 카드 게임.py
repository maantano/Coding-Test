# n = 3
# m = 3
# arr = [[3,1,2],[4,1,4],[2,2,2]]

# n = 2
# m = 4
# arr = [[7,3,1,8],[3,3,3,4]]

# 내 풀이
n,m = map(int,input().split())
answer = []
arr = []
for i in range(n):
	arr.append(list(map(int,input().split())))
	answer.append(min(arr[i]))
print(max(answer))


# 책 풀이
n,m = map(int,input().split())
result = 0
for i in range(n):
	arr = (list(map(int,input().split())))
	min_v = min(arr)
	result = max(result,min_v)
print(result)
