import sys
input = sys.stdin.readline
n = int(input())
def prime(s):
	if s == 1:
		return False
	for i in range(2,int(s**0.5)+1):
		if s % i == 0:
			return False
	return True

idx = n
while True:
	if prime(idx) and str(idx) == ''.join(reversed(str(idx))):
		print(idx)
		break
	idx+=1
