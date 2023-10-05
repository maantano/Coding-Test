

n = 7
m = 2
arr = [1,1,2,2,2,2,3]

def count_by_value(arr,x):
	n = len(arr)
	a = first(arr,x,0,n-1)
	print('a =====>',a)
	if a == None:
		return 0
	b = last(arr,x,0,n-1)
	print('b =====>',b)
	return b-a+1

def first(arr,target,start,end):
	if start > end:
		return None
	mid = (start+end) // 2
	print('first | | mid,start,end ===>',mid,start,end)
	if (mid == 0 or target > arr[mid-1]) and arr[mid] == target:
		print('finally')
		return mid
	elif arr[mid] >= target:
		return first(arr,target,start,mid-1)
	else:
		return first(arr,target,mid+1,end)

def last(arr,target,start,end):
	if start > end:
		return None
	mid = (start+end) // 2
	print('last | | mid,start,end ===>',mid,start,end)
	if (mid == n -1 or target < arr[mid+1]) and arr[mid] == target:
		print('finally')
		return mid
	elif arr[mid] > target:
		return last(arr,target,start,mid-1)
	else:
		return last(arr,target,mid+1,end)



n,x = map(int,input().split())
arr = list(map(int,input().split()))

count = count_by_value(arr,x)

if count == 0:
	print(-1)
else:
	print(count)
