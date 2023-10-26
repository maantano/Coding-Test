while True:
	n = input()
	stack = []
	if len(n) == 1 and n =='.':
		break

	for i in n:
		if i == '[' or i == '(':
			stack.append(i)
		elif i == ']':
			if stack and stack[-1] == '[':
				stack.pop()
			else:
				stack.append(']')
				break
		elif i == ')':
			if stack and stack[-1] == '(':
				stack.pop()
			else:
				stack.append(')')
				break
	if not stack:
		print('yes')
	else:
		print('no')

