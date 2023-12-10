import sys
input = sys.stdin.readline

cnt = 0
chk = 1000 - int(input())

while chk:
	if chk // 500:
		cnt += chk //500
		chk -= (chk // 500) * 500
	elif chk // 100:
		cnt += chk //100
		chk -= (chk // 100) * 100
	elif chk // 50:
		cnt += chk //50
		chk -= (chk // 50) * 50
	elif chk // 10:
		cnt += chk //10
		chk -= (chk // 10) * 10
	elif chk // 5:
		cnt += chk //5
		chk -= (chk // 5) * 5
	elif chk // 1:
		cnt += chk //1
		chk -= (chk // 1) * 1
print(cnt)
