# 4 11
# 802
# 743
# 457
# 539

n,k = map(int,input().split())

arr = []
for i in range(n):
	arr.append(int(input()))
tmpEnd = max(arr) // 100
l = []

for i in range(1,tmpEnd+1):
	l.append(100*i)
arr.sort()

start = l[0]
end = l[-1]

while start <= end:
	count = 0
	mid = (start+end) // 2
	for i in arr:
		count +=  (i // mid)
	if count <= k:
		end = mid -50
	elif count >= k:
		start = mid +50
	if count == k:
		break
print(mid)


# n,k = map(int,input().split())

# arr = []
# for i in range(n):
# 	arr.append(int(input()))
# start = 100
# # end = max(arr) // 100 * 100
# end = 100 * int(str(max(arr))[0])
# while start <= end:
# 	count = 0
# 	mid = (start+end) // 2
# 	print('mid ====>',mid)
# 	for i in arr:
# 		count +=  (i // mid)
# 		print('tmp count ===>',count)
# 	print('total count ===>',count)
# 	if count <= k:
# 		end = mid -50
# 	elif count >= k:
# 		start = mid +50
# 	if count == k:
# 		break
# 	print('==========================')

# print(mid)


