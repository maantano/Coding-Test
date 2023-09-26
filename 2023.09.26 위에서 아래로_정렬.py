n = int(input())

stack = []
for i in range(n):
	v = int(input())
	stack.append(v)

stack = sorted(stack,reverse=True)

for i in stack:
	print(i)
