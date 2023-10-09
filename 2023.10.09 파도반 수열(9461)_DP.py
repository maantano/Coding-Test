
n = int(input())
arr = []

for i in range(n):
	arr.append(int(input()))


d = [0] * 101

d[0] = 0
d[1] = 1
d[2] = 1
d[3] = 1


for i in arr:
	for j in range(4,i+1):
		d[j] = d[j-2]+d[j-3]


for i in arr:
	print(d[i])

