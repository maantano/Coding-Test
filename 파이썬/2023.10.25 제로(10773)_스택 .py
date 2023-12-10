import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
	tmp = int(input().rstrip())
	if tmp == 0:
		arr.pop()
	else:
		arr.append(tmp)
print(sum(arr))
