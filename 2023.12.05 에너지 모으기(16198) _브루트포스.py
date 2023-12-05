# import sys
# input = sys.stdin.readline


# n = int(input())
# arr = list(map(int,input().split()))
# answer = 0
# while True:
# 	tmp = -int(1e9)
# 	idx = 0
# 	if len(arr) == 3:
# 		answer += (arr[0] * arr[-1])
# 		print(answer)
# 		break
# 	for i in range(1,len(arr)-1):
# 		if tmp <= arr[i-1]*arr[i+1]:
# 			idx  = i
# 			tmp = arr[i-1]*arr[i+1]
# 	answer +=tmp
# 	arr.remove(arr[i])
# 	print(answer)
# 	print(arr)


import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int,input().split()))
answer = 0

def bt(x):
	global answer
	if len(arr) == 2:
		answer = max(answer,x)
		return

	for i in range(1,len(arr)-1):
		target = arr[i-1] * arr[i+1]

		chk = arr.pop(i)
		bt(x+target)
		chk = arr.insert(i,chk)

bt(0)
print(answer)

