# 2 2
# 3 5
# 2 9

# 4 3
# 2 3 5 9
# 1 4 7
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))

# arr.sort(reverse=True)
# arr2.sort(reverse=True)
# p1 = n-1
# p2 = m-1
# answer = []
# while p1>=0 and p2>=0:
# 	if arr[p1] > arr2[p2]:
# 		tmp = arr2.pop()
# 		answer.append(tmp)
# 		p2-=1

# 	elif arr[p1] < arr2[p2]:
# 		tmp = arr.pop()
# 		answer.append(tmp)
# 		p1-=1
# 	else:
# 		answer.append(arr.pop())
# 		answer.append(arr2.pop())
# 		p2-=1
# print(*answer+arr2+arr)


import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr.sort()
arr2.sort()
p1 = 0
p2 = 0
answer = []
while p1 != n or p2 != m:
	if p1 == n:
		answer.append(arr2[p2])
		p2+=1
	elif p2 == m:
		answer.append(arr[p1])
		p1+=1
	else:
		if arr[p1] < arr2[p2]:
			answer.append(arr[p1])
			p1+=1
		else:
			answer.append(arr2[p2])
			p2+=1
print(*answer)
