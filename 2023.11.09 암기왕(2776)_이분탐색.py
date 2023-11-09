import sys
input = sys.stdin.readline

t = int(input())

def binarySearch(s,e,nums1,num):
	while s <= e:
		mid = (s+e) // 2

		if nums1[mid] == num:
			return 1
		elif nums1[mid] < num:
			s = mid + 1
		else:
			e = mid - 1
	return 0


for i in range(t):
	n1 = int(input())
	arr1 = sorted(map(int,input().split()))
	n2 = int(input())
	arr2 = map(int,input().split())

	for num in arr2:
		print(binarySearch(0,n1-1,arr1,num))
