import sys
input = sys.stdin.readline
n = int(input())
nL = list(map(int,input().split()))
nL.sort()
m = int(input())
mL = list(map(int,input().split()))




for i in mL:
	lt,rt = 0, n-1
	chk = False
	while lt <= rt:
		mid = (lt+rt) // 2
		if i== nL[mid]:
			chk = True
			print(1)
			break
		if i > nL[mid]:
			lt = mid + 1
		else:
			rt = mid - 1
	if not chk:
		print(0)
