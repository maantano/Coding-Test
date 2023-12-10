import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

for i in arr:
	cnt1 = 0
	cnt2 = 0
	cnt3 = 0
	cnt4 = 0
	if i // 25:
		cnt1 = i // 25
		i -= (i//25) * 25
	if i // 10:
		cnt2 = i // 10
		i -= (i//10) * 10
	if i // 5:
		cnt3 = (i // 5)
		i -= (i//5) * 5
	if i // 1:
		cnt4 = (i // 1)
		i -= (i//1) * 1
	print(cnt1,cnt2,cnt3,cnt4,sep=' ')


# for i in range(n):
# 	print(cnt1[i],cnt2[i],cnt3[i],cnt4[i],sep=' ')
