# T = int(input())

# def chkA(tmp):
# 	return tmp+'a'
# 	# return [tmp+'a','a'+tmp]

# def chkB(tmp,aCnt):
# 	tmp = ('b'*aCnt)+tmp+('b'*aCnt)
# 	return tmp

def solution(s):
	answer = []
	for a in s:
		tmp = ''
		if len(a) % 2 == 0:
			start = len(a) // 2
		else:
			start = (len(a) // 2) - 1

		if len(a[:start]) >= len(a[start:]):
			flag = True
			tmp = a[start:]
		else:
			flag = False
			tmp = 'a'+a[:start][::-1]
		while True:
			if flag:
				print('a[:start]>',a[:start])
				print('tmp>',tmp)
				if a[:start] == tmp:
					answer.append(True)
					break
				else:
					if len(tmp) > len(a[:start]):
						answer.append(False)
						break
					else:
						tmp = tmp+'a'
			else:
				print('===============')
				print('a[start:]>',a[start:])
				print('tmp>',tmp)
				if a[start:] == tmp:
					answer.append(True)
					break
				else:
					if len(tmp) > len(a[start:]):
						answer.append(False)
						break
					else:
						tmp = tmp+'a'

	return answer



a = ['abab','bbaa','bababa','bbbabababbbaa']
print(solution(a))








			# aCnt = a.count('a')
			# tmpCnt = tmp.count('a')
			# if aCnt == ('b'*tmpCnt)+tmp+('b'*tmpCnt).count('a'):
			# 	if a == chkB(tmp,tmpCnt):
			# 		answer.append('true')
			# 	else:
			# 		answer.append('false')

			# elif aCnt == ('a'+tmp).count('a'):
			# 	if a ==






# def solution(s):
# 	answer = []
# 	for a in s:
# 		tmp = 'a'
# 		while True:
# 			aCnt = a.count('a')
# 			# if tmp == a:
# 			# 	answer.append('true')
# 			# 	break

# 			tmpCnt = tmp.count('a')

# 			if aCnt == ('b'*tmpCnt)+tmp+('b'*tmpCnt).count('a'):
# 				if a == chkB(tmp,tmpCnt):
# 					answer.append('true')
# 				else:
# 					answer.append('false')

# 			elif aCnt == ('a'+tmp).count('a'):
# 				if a ==








			# tmp = chkB(tmp,tmpCnt)
			# tmp2 =  chkA(tmp)
			# if

			# if len(tmp) > len(a) and len(tmp2) > len(a):
			# 	answer.append('false')
			# 	break





			# for j in a:
			# 	if j == 'a':
			# 		stack.append(j)
			# 	elif j == 'b':
			# 		if stack:
			# 			stack.pop()
			# 		else: # 스택에 괄호가 없을경우 NO
			# 			print("NO")
			# 			break
			# else: # break문으로 끊기지 않고 수행됬을경우 수행한다
			# 	if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
			# 		print("YES")
			# 	else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
			# 		print("NO")




def getPi(pattern):
    p = [0] * len(pattern)
    correct_cnt = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[correct_cnt]:
            correct_cnt += 1
        else:
            if correct_cnt > 0:
                correct_cnt = p[correct_cnt - 1]
                i -= 1
                continue
        p[i] = correct_cnt
    return p

def kmp(p, pattern, sentence):
    correct_cnt = 0
    pattern_len = len(pattern)
    for i in range(len(sentence)):
        if sentence[i] == pattern[correct_cnt]:
            correct_cnt += 1
        else:
            if correct_cnt > 0:
                correct_cnt = p[correct_cnt - 1]
                i -= 1
        if correct_cnt == pattern_len:
            return i
    return -1

sentence = input()
pattern = input()

p = getPi(pattern)

print(kmp(p, pattern, sentence))
