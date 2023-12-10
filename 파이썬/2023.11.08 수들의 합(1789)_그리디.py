import sys
input = sys.stdin.readline


s = int(input())

answer = 0
chk = 0
tmp =1
while True:
	if chk > s:
		break
	chk += tmp
	tmp+=1
	answer+=1
print(answer-1)
