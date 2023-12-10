# n,m = map(int,input())

# arr = []
# for i in range(n):
# 	arr.append(int(input()))

n = 2
m = 15
arr = [2,3]

d = [10001] * (m+1)

d[0] = 0


for i in range(n):
	for j in range(arr[i],m+1):
		if d[j - arr[i]] != 10001:
			d[j] = min(d[j],d[j-arr[i]] + 1)
if d[m] == 10001:
	print(-1)
else:
	print(d[m])



# for i in range(3,n+1):
# 	if m == 0:
# 		break
# 	else:
# 		cnt = -1
# 	d[i] = d[i-]



