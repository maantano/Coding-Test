

# 재귀 함수
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
targetL = list(map(int,input().split()))

def bs(arr,target,start,end):
	if start > end:
		return None
	# while start <= end:
	mid = (start+end) // 2
	if arr[mid] == target:
		return mid
	elif arr[mid] < target:
		return bs(arr,target,mid+1,end)
	else:
		return bs(arr,target,start,mid-1)
for i in range(m):
	result = bs(arr,targetL[i],0,n-1)
	if result != None:
		print('yes',end = ' ')
	else:
		print('no',end = ' ')


# 반복문

def bs(arr,target,start,end):
	while start <= end:
		mid = (start+end) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			end = mid - 1
		else:
			start = mid +1
	return None

n = int(input())

arr = list(map(int,input().split()))

arr.sort()

m = int(input())

x = list(map(int,input().split()))

for i in x:
	result = bs(arr,i,0,n-1)
	if result != None:
		print('yes', end = ' ')
	else:
		print('no', end = ' ')


# 계수 정렬

n = int(input())

arr = 100001 * [0]

for i in input().split():
	arr[int(i)] = 1
m = int(input())
x = list(map(int,input().split()))

for i in x:
	if arr[i] == 1:
		print('yes',end = ' ')
	else:
		print('no',end = ' ')


# 집합 자료형 이용(set())

n = int(input())

arr = set(map(int,input().split()))

arr.sort()

m = int(input())

x = list(map(int,input().split()))

for i in x:
	if i in arr:
		print('yes', end = ' ')
	else:
		print('no', end = ' ')
