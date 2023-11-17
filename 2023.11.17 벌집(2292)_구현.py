

import sys
input = sys.stdin.readline

n = int(input())
nums_pileup = 1
cnt = 1
while n > nums_pileup:
	nums_pileup += 6 * cnt
	cnt+=1
print(cnt)



# import sys
# input = sys.stdin.readline

# n = int(input())
# chk = 1
# cnt = 1
# while True:
# 	if n == 1:
# 		print(n)
# 		break
# 	chk += (6*cnt)
# 	if n <= chk:
# 		print(cnt+1)
# 		break
# 	cnt+=1
