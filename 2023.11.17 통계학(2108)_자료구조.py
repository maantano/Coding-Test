import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input().rstrip()) for _ in range(n)])
print(round(sum(arr) / len(arr)))
print(arr[len(arr)//2])

d = {}
for i in arr:
	if i in d:
		d[i] +=1
	else:
		d[i] = 1

mx = max(d.values())
mx_d = []

for i in d:
	if mx == d[i]:
		mx_d.append(i)

if len(mx_d) > 1:
	print(mx_d[1])
else:
	print(mx_d[0])


print(max(arr)-min(arr))
