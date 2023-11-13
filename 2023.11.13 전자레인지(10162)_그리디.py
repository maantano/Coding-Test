import sys
input = sys.stdin.readline


chk = int(input())

cnt1 = 0
cnt2 = 0
cnt3 = 0
posi = True
while chk:
	if 0< chk < 10:
		posi = False
		break

	if chk // 300:
		cnt1+= chk // 300
		chk -= chk // 300 * 300
	if chk // 60:
		cnt2+= chk // 60
		chk -= chk // 60 * 60
	if chk // 10:
		cnt3+= chk // 10
		chk -= chk // 10 * 10
if posi:
	print(cnt1,cnt2,cnt3,sep=' ')
else:
	print(-1)
