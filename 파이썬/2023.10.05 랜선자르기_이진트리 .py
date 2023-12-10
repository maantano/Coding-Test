# 4 11
# 802
# 743
# 457
# 539

# n,k = map(int,input().split())

# arr = []
# for i in range(n):
# 	arr.append(int(input()))
# tmpEnd = max(arr) // 100
# l = []

# for i in range(1,tmpEnd+1):
# 	l.append(100*i)
# arr.sort()

# start = l[0]
# end = l[-1]

# while start <= end:
# 	count = 0
# 	mid = (start+end) // 2
# 	for i in arr:
# 		count +=  (i // mid)
# 	if count <= k:
# 		end = mid -50
# 	elif count >= k:
# 		start = mid +50
# 	if count == k:
# 		break
# print(mid)


k,n = map(int,input().split())
arr = []
for i in range(k):
	arr.append(int(input()))
start = 1
end = max(arr)

while start <= end:
	mid = (start+end) // 2
	count = 0
	print('start ====>',start)
	print('end ====>',end)
	print('mid ====>',mid)
	for i in range(k):
		count += arr[i] // mid
	print('count =====>',count)
	if count >= n:
		start = mid + 1
	else:
		end = mid - 1
	print('-------------정신차려!----------------')
print(end)



