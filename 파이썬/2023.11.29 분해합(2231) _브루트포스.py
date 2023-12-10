# import sys
# input = sys.stdin.readline

# n = input().rstrip()
# for i in range(10**(len(n)-1),int(n)):
# 	tmp = 0
# 	for j in range(len(n)):
# 		tmp += int(str(i)[j])
# 	if tmp+i == int(n):
# 		print(i)
# 		break

# for i in range(int(n),1,-1):
# 	tmp = 0
# 	if len(str(i)) < len(n):
# 		break
# 	for j in range(len(n)):
# 		tmp += int(str(i)[j])
# 	if

n = int(input())

for i in range(1, n+1):
	num = sum((map(int, str(i))))
	num_sum = i + num
	if num_sum == n:
		print(i)
		break
	if i == n:
		print(0)
