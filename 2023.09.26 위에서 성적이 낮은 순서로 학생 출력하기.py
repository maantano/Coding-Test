n = int(input())
stack = []

for i in range(n):
	k,v = input().split()
	stack.append((k,v))

stack = sorted(stack, key=lambda x : x[1])

for i in stack:
	print(i[0], end = ' ')
