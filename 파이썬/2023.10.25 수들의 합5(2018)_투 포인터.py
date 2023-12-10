import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
lp = 0
rp = 0
tmp = 0
while rp <=n:
	if tmp < n:
		rp+=1
		tmp+=rp
	elif tmp > n:
		lp +=1
		tmp -= lp
	else:
		cnt+=1
		rp+=1
		tmp+=rp

print(cnt)
