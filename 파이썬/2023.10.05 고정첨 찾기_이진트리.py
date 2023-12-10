# n = int(input())
n = 5
# arr = list(map(int,input().split()))
arr = [-15,-6,1,3,7]

# def first(arr,target,start,end):
# 	mid = (start+end) // 2
# 	if start > end:
# 		return None
# 	if arr[mid] >= target:
# 		return first(arr,target,start,mid-1)
# 	elif arr[mid] < target:
# 		return first(arr,target,mid+1,end)
# 	elif (mid == 0 or target > arr[mid-1]) and arr[mid] == target:
# 		return mid

# def last(arr,target,start,end):
# 	mid = (start+end) // 2
# 	if start > end:
# 		return None
# 	if arr[mid] > target:
# 		return last(arr,target,start,mid-1)
# 	elif arr[mid] < target:
# 		return last(arr,target,mid+1,end)
# 	elif (mid == n-1 or target < arr[mid+1]) and arr[mid] == target:
# 		return mid


def point(arr,start,end):


	if start>end:
		return None

	mid = (start+end) // 2

	if mid == arr[mid]:
		return mid
	elif arr[mid] > mid:
		return point(arr,start,mid-1)
	else:
		return point(arr,mid+1,end)
	# elif mid < arr[mid]:
	# 	return point(arr,mid+1,end)
	# else:
	# 	print(-1)



idx = point(arr,0,n-1)

if idx == None:
	print(-1)
else:
	print(arr[idx])
