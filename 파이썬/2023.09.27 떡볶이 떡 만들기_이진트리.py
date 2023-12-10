# # n,m = map(int,input().split())
# # arr = list(map(int,input().split()))

# n = 4
# m = 6

# arr = [19,15,10,17]
# arr.sort()
# start = arr[0]
# end = arr[-1]

# def bs(arr,target,start,end):
# 	mid = (arr[0] + arr[-1]) // 2
# 	result = 0
# 	for i in range(n):
# 		result += (arr[i] - mid)
# 		if result == target:
# 			return result
# 		elif result > target:
# 			return bs(arr,target,mid+1,end)
# 		else:
# 			return  bs(arr,target,start,mid-1)

# print(bs(arr,m,start,end))





# n,m = map(int,input().split())
# arr = list(map(int,input().split()))

n = 4
m = 6

arr = [19,15,10,17]
# arr.sort()
start = 0
end = max(arr)
# end = arr[-1]

result = 0
while (start<=end):
	total= 0
	mid = (start + end) // 2
	for x in arr:
		if x > mid:
			total += (x - mid)
	if total < m:
		end = mid-1
	else:
		start = mid + 1
		result = mid




print(result)





