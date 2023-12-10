
import sys
input = sys.stdin.readline
from collections import deque

a,b = map(int,input().split())
q = deque([(a,1)])
chk = False
while q:
	now,cnt = q.popleft()
	if now == b:
		# print(cnt)
		chk = True
		break
	if now * 2 <= b:
		q.append((now*2,cnt+1))
	if now * 10 + 1 <= b:
		q.append((now*10+1,cnt+1))
if chk:
	print(cnt)
else:
	print(-1)




# print(int(str(4)+'1'))
