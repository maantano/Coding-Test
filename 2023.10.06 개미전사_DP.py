# n = int(input())

# arr = list(map(int,input().split()))
n = 4
arr = [1,3,1,5]
d = [0] * 100

d[0] = arr[0]
d[1] = max(arr[0],arr[1])

for i in range(2,n):
	d[i] = max(d[i-1],d[i-2]+arr[i])
print(d)


# def g():
# 	tmp = 0
# 	for i in range(n):
# 		for j in range(i+2,n):
# 			d[i+j] = arr[i] + arr[j]
# g()
# print(max(d))



