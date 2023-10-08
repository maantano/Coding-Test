n,k = map(int,input().split())
arr = []
for i in range(n):
	arr.append((int(input())))

d = [0] * (k+1)

d[0] = 1
for i in arr:
	for j in range(i,k+1):
		if j-i >= 0:
			d[j] += d[j-i]

print(d[k])


# n,k = map(int,input().split())
# arr = []
# for i in range(n):
# 	arr.append((int(input())))

# d = [0] * (k+1)

# d[0] = 1
# for i in arr:
# 	for j in range(i,k+1):
# 		d[j] += d[j-i]

# print(d[k])
