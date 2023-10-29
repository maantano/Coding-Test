import sys
input = sys.stdin.readline

word = input().strip()
if word[0] == 'c':
	answer= 26
else:
	answer = 10

for i in range(1,len(word)):
	if word[i] == 'c':
		if word[i-1] == 'c':
			answer*=25
		else:
			answer*=26
	else:
		if word[i-1] == 'd':
			answer*=9
		else:
			answer*=10
print(answer)
# cnt = 1
# stack = []
# for i in word:
# 	if stack:
# 		j = stack[-1]

# 		if i == 'd':
# 			if j[0] == 'd':
# 				stack.append(['d',j[1]-1])
# 			else:
# 				stack.append(['d',10])
# 		else:
# 			if j[0] == 'c':
# 				stack.append(['c',j[1]-1])
# 			else:
# 				stack.append(['c',26])
# 	else:
# 		if i == 'c':
# 			stack.append(['c',26])
# 		else:
# 			stack.append(['d',10])
# for i in stack:
# 	cnt *=i[1]
# print(cnt)
