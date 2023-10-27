# import sys
# input = sys.stdin.readline

# n = list(input().split())
# stack = []
# l = 0
# r = 0
# cnt= 0
# while n:
# 	while stack:
# 		if stack[-1] == ')':
# 			for i in stack:
# 			stack.pop()

# 	# if stack:
# 	# 	a = stack.pop()

# 		# if a == '(':
# 		# 	while stack:
# 		# 		if stack.pop() == ')':
# 		# 			break
# 		# 		else:
# 		# 			cnt+=1

# 		# while stack:
# 	else:
# 		stack.append(n.pop(0))

import sys
input = sys.stdin.readline

n = list(input().rstrip())
stack = []

ret = 0
for c in n:
	if c == '(':
		stack.append(c)
	else:
		if stack:
			stack.pop()
		else:
			ret+=1
print(ret + len(stack))

# import sys

# s = input()
# while '()' in s:
# 	s = s.replace('()', "")
# print (len(s))

