# import sys
# input = sys.stdin.readline

# answer = []
# while True:
# 	word = input().rstrip()
# 	if '-' in word:
# 		break
# 	stack = []
# 	cnt = 0
# 	for i in word:
# 		if i =='{':
# 				stack.append(i)
# 		else:
# 			if stack[-1:] == ['{']:
# 				stack.pop()
# 			else:
# 				stack.append(i)
# 	while stack:
# 		a = stack.pop()
# 		if a =='}':
# 			if stack[-1] == '{':
# 				stack.pop()
# 				cnt+=2
# 			else:
# 				stack.pop()
# 				cnt+=2
# 		else:
# 			if stack[-1] == '}':
# 				stack.pop()
# 				cnt+=2
# 			else:
# 				stack.pop()
# 				cnt+=1
# 	answer.append(cnt)



answer = []

while True:
	stack = []
	count = 0
	s = input()
	if '-' in s:
		break
	for i in range(len(s)):
		if not stack and s[i] == '}':
			count+=1
			stack.append('{')
		elif stack and s[i] == '}':
			stack.pop()
		else:
			stack.append(s[i])
	count += len(stack) // 2
	answer.append(count)

for i in range(len(answer)):
	print(i+1,'. ',answer[i], sep='')

