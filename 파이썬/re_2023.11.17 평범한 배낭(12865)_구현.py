# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = []
# for i in range(n):
# 	arr.append(list(map(int,input().split())))

# arr.sort(key=lambda x: x[0])

# for i in range(n):
# 	tmp = arr[i][0]
# 	answer = arr[i][1]
# 	m-=tmp
# 	for j in range(i):
# 		if m >= tmp:
# 			tmp+=arr[j][0]
# 			m -= arr[j][1]
# 	answer = max(answer,tmp)
# print(answer)



import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
	stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
	for j in range(1, K + 1):
		weight = stuff[i][0]
		value = stuff[i][1]

		if j < weight:
			knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
		else:
			knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])

