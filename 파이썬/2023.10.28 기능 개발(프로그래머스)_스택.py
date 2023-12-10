
# p = [93, 30, 55]
# s = [1, 30, 5]
# [2, 1]
p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]
# [1, 3, 2]


# def solution(p,s):
# 	stack = []
# 	answer= []
# 	for i in range(len(p)):
# 		a = ((100 -p[i]) // s[i]) if (100 -p[i]) % s[i] == 0 else ((100 -p[i]) // s[i])+1
# 		stack.append(a)

# 	stack.reverse()
# 	a = stack.pop()
# 	cnt = 1
# 	while stack:
# 		if a > stack[-1]:
# 			cnt+=1
# 			stack.pop()
# 		else:
# 			cnt = 1
# 			a = stack.pop()
# 		answer.append(cnt)

# 	print(answer)
# solution(p,s)


def solution(p,s):
	answer=  []
	days = 0
	cnt = 0

	while len(p) > 0:
		if p[0]+days * s[0] >= 100:
			p.pop(0)
			s.pop(0)
			cnt+=1
		else:
			if cnt > 0:
				answer.append(cnt)
				cnt = 0
			else:
				days+=1
	answer.append(cnt)
	return answer
solution(p,s)
