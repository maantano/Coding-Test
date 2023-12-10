# 시간 초과
# n = list(input().rstrip())
# cur = len(n)
# m = int(input())
# for _ in range(m):
# 	c = list(input().split())
# 	if c[0] == 'P':
# 		n.insert(cur,c[1])
# 		cur+=1
# 	elif c[0] == 'L':
# 		if cur != 0:
# 			cur-=1
# 	elif c[0] == 'D':
# 		if cur < len(n):
# 			cur+=1
# 	else:
# 		if cur >0:
# 			n.remove(n[cur-1])
# print(''.join(n))


import sys

stack_l = list(input())
stack_r = []
n = int(input())

for i in range(n):
	command = sys.stdin.readline().split()

	if command[0] == "L" and stack_l:
		stack_r.append(stack_l.pop())
	elif command[0] == "D" and stack_r:
		stack_l.append(stack_r.pop())
	elif command[0] == "B" and stack_l:
		stack_l.pop()
	elif command[0] == "P":
		stack_l.append(command[1])

print("".join(stack_l + list(reversed(stack_r))))
