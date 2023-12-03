import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())


arr = []
for i in range(n):
	arr.append(list(map(int,input().split())))

combi = []
for i in range(1,n+1):
	combi.append(combinations(arr,i))

answer = int(1e9)

for line in combi:
	for each in line:
		sour = 1
		bitter = 0
		for e in each:
			sour *= e[0]
			bitter += e[1]
		answer = min(answer,abs(sour - bitter))
print(answer)





# import sys
# input = sys.stdin.readline
# n = int(input())

# sl = []
# bl = []

# for i in range(n):
# 	s,b = map(int,input().split())
# 	sl.append(s)
# 	bl.append(b)

# dp = [int(1e9)] * (n)
# dps = [int(1e9)] * (n)
# dps[0] = sl[0]
# dpb = [int(1e9)] * (n)
# dpb[0] = bl[0]


# for i in range(1,n):
# 	print('sl[i] * dps[i-1] ===>',sl[i] * dps[i-1])
# 	print('dps[i] ===>',dps[i])
# 	print('bl[i] + dpb[i-1],dpb[i] ===>',bl[i] + dpb[i-1],dpb[i])
# 	print('dpb[i] ===>',dpb[i])
# 	print('-------------------------------------------------------')

# print(dps)
# print(dpb)



# # dp = [int(1e9)] * n
# for i in range(1,n):
# 	for j in range(1,n):
# 		dps[i] = min(sl[j] * dps[i-1],dps[i])
# 		dpb[i] = min(bl[j] + dpb[i-1],dpb[i])
# 		# dp[i] = min(dp[i],abs(sl[j] * dps[j-1] - bl[j] + dpb[j-1]))
# print(dps)
# print(dpb)
