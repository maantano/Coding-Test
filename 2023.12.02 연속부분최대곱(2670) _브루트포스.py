import sys
input = sys.stdin.readline

# n = 8
# arr = [1.1, 0.7, 1.3, 0.9, 1.4, 0.8, 0.7, 1.4]
n = int(input())
arr = [float(input()) for _ in range(n)]
for i in range(1, n):
	arr[i] = max(arr[i], arr[i] * arr[i - 1])
print('%0.3f' % max(arr))







