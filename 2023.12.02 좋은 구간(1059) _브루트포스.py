import sys
input = sys.stdin.readline
l = int(input())
arr = sorted(list(map(int,input().split())))
n = int(input())
target = []
for i in range(l-1):
	tmp = []
	for j in range(1,max(arr)+1):
		if arr[i] < j < arr[i+1]:
			tmp.append(j)
	target.append(tmp)

targetL = []
for i in target:
	if i[0]<= n <= i[-1]:
		targetL = i
		break
cnt =0
for i in range(len(targetL)):
	for j in range(len(targetL)):
		if i == j:
			continue
		if targetL[i]<= n <= targetL[j]:
			cnt+=1
print(cnt)



import sys
L = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
nums.sort()

if n in nums:
	print(0)
else:
	min = 0
	max = 0
	for num in nums:
		if num < n:
			min = num
		elif num > n and max == 0:
			max = num
	max -= 1
	min += 1
	print((n-min)*(max-n+1) + (max-n))


L = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.append(0)
nums.sort()

A = 0
for i in range(len(nums)-1) :
	if nums[i] == target or nums[i+1] == target:
		A = 0
		break
	elif nums[i] < target and target < nums[i+1]:
		A = (target - nums[i]) * (nums[i+1] - target) - 1
		break

print(A)
