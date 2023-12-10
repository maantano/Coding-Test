import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))


a = sum(arr[:m])
answer = [a]
for i in range(n-m):
	answer.append(answer[i] - arr[i]+arr[i+m])
print(max(answer))


# import sys
# input = sys.stdin.readline

# n, k = map(int,input().split())
# a = list(map(int, input().split()))

# result = []
# result.append(sum(a[:k]))

# for i in range(n - k):
#     result.append(result[i] - a[i] + a[k+i])

# print(max(result))
