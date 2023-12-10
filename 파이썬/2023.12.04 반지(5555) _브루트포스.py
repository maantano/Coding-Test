import sys
input = sys.stdin.readline

stamp = input().rstrip()
n = int(input())
answer = 0
for i in range(n):
	tmp = input().rstrip()
	if len(tmp.split(stamp)) == 1 :
		if stamp in (tmp * 2):
			answer += 1
	else:
		answer += 1
print(answer)


