import sys
n = int(input())
stack = []
cnt =1


l = list(map(int,input().split()))

while l:
	if cnt == l[0]:
		cnt+=1
		l.pop(0)
	else:
		stack.append(l.pop(0))
	while stack:
		if stack[-1] == cnt:
			stack.pop()
			cnt+=1
		else:
			break
if len(stack) == 0:
	print('Nice')
else:
	print('Sad')
