n = int(input())
arr = list(map(int,input().split()))
arr.sort()

answer = []
for i in range(n):
	result = 0
	for j in range(n):
		result += abs(arr[i] - arr[j])
	answer.append(result)


print(arr[answer.index(min(answer))])





n = int(input())
data = list(map(int,input().split()))
data.sort()


print(data[(n-1)//2])

