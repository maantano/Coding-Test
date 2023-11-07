
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

def nextPermutation(list_a):

	k = -1
	m = -1

	for i in range(len(list_a)-1):
		if list_a[i] < list_a[i+1]:
			k = i

	if k == -1:
		return [-1]

	for i in range(k,len(list_a)):
		if arr[k] < arr[i]:
			m = i

	arr[m],arr[k] = arr[k],arr[m]
	list_a = list_a[:k+1] + sorted(list_a[k+1:])

	return list_a


print(*nextPermutation(arr))
