import sys
input = sys.stdin.readline
from collections import deque
n,m,k = map(int,input().split())
se = list(map(str,input().split()))
chk = list(map(str,input().split()))

if m < n:
	print('normal')
	exit()
secret = ''.join(se)
chk = ''.join(chk)
if secret in chk:
	print('secret')
else:
	print('normal')








