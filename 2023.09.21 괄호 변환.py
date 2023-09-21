w = '(()())()'
# w = ')('
# w = '()))((()'




# u = []
# v = []

# stack =[]
# for i in w:


def balance_index(p):
	count = 0
	for i in range(len(p)):

		if p[i] == '(':
			count +=1
		else:
			count -=1
		if count == 0:
			return i

# balance_index(w)
def chk_proper(p):
	count = 0
	for i in p:
		if i == '(':
			count +=1
		else:
			if count == 0:
				return False
			count -=1
	return True


def solution(p):
	answer =''
	if p == '':
		return answer
	index = balance_index(p)
	u = p[:index+1]
	v = p[index+1:]

	if chk_proper(u):
		answer = u + solution(v)
	else:
		answer = '('
		answer += solution(v)
		answer += ')'
		u = list(u[1:-1]) # 첫 문자와 마지막 문자 제거
		for i in range(len(u)):
			if u[i] == '(':
				u[i] = ')'
			else:
				u[i] = '('
		answer += "".join(u)
	print(answer)
	return answer




solution(w)
