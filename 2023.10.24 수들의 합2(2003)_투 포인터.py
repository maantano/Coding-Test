# 4 2
# 1 1 1 1

# 10 5
# 1 2 3 4 2 5 3 1 1 2

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))

p1 = 0
p2 = 1
cnt = 0
while p2 <= n and p1 <= p2:
		sums = arr[p1:p2]
		total = sum(sums)
		if total == m:
			cnt +=1
			p2 += 1
		elif total < m:
			p2 +=1
		else:
			p1+=1
print(cnt)

# for i in range(n-1):
# 	if arr[p1] + arr[p2] < m:
# 		p1+=1
# 	elif arr[p1] + arr[p2] > m:
# 		p2+=1
# 	else:
# 		p1+=1
# 		p2+=1
# 		cnt+=1


