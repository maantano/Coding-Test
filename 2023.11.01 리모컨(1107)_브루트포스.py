
# target = input()

# n = int(input())
# miss = list(map(int,input().split(' ')))

# # 5455++ 또는 5459--
# cnt = 0
# for i in range(len(target)):
# 	tmp = int(arr[i])
# 	btnClick = 0
# 	minusTmp,plusTmp = tmp-1,tmp+1

# 	while tmp in miss:
# 		if minusTmp in not in miss:
# 			btnClick +=2
# 			tmp = minusTmp
# 			break
# 		elif plusTmp in not in miss:
# 			btnClick +=2
# 			break
# 		else:
# 			minusTmp-=1
# 			plusTmp+=1
# 	cnt+=btnClick


# 	if arr[i] in miss:

# 작거나 큰경우를 같이 비교해야 하는 경우???



# import sys
# input = sys.stdin.readline

# target= input()
# n = int(input().rstrip())
# miss = list(map(int,input().split(' ')))

# cnt = 0
# if target == '100':
# 	print(0)
# else:
# 	for i in range(len(target),0,-1):
# 		chk = int(arr[i])

# 		if chk in miss:
# 			if chk -1 not in miss:

# 			elif chk +1 not in miss:

# 			else:



# 		else:
# 			target -= chk * (10 ** (i-1))
import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
break_num= list(map(int, input().split()))
min_count = abs(100 - target)

for nums in range(1000001):
	nums = str(nums)
	for j in range(len(nums)):
		if int(nums[j]) in break_num:
			break
		elif j == len(nums) - 1:
			min_count = min(min_count, abs(int(nums) - target) + len(nums))
print(min_count)

#최대한 제일 가까이 까지 가서,고장난 버튼 안에 없는 다른 버튼을 무조건 len(nums)만큼은 눌러야 하니까 더하고

