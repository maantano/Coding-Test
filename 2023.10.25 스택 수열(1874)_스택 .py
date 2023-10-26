import sys
input = sys.stdin.readline

n = int(input())
arr =list(range(1,n+1))

count = 1
stack = []
op = []
tmp = True
for i in range(n):
	num = int(input())

	while count <= num:
		stack.append(count)
		count+=1
		op.append('+')
	if stack[-1] == num:
		stack.pop()
		op.append('-')
	else:
		tmp = False
		break
if tmp:
	for j in op:
		print(j)
else:
	print('NO')



