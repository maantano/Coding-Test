
# 보이스루
# 1번.
# arr = [1, 1, 3, 3, 0, 1, 1]
# ans = [1, 3, 0, 1]

# answer = [arr[0]]
# pos = arr[0]
# for i in range(1,len(arr)):
# 	if pos == arr[i]:
# 		continue
# 	else:
# 		pos = arr[i]
# 		answer.append(arr[i])
# print(answer)


# 2번



# cnt = 0
# for skill_tree in skill_trees:
# 	s = ''
# 	for chk in skill_tree:
# 		print(chk)
# 		if chk in skill:
# 			s += chk
# 	if skill[:len(s)] == s:
# 		cnt+=1
# print(cnt)


# def solution(skill, skill_trees):
# 	count = 0
# 	for skill_tree in skill_trees:
# 		s = ""                      # 하나의 스킬트리를 뽑을 때마다 s 초기화
# 		for ch in skill_tree:
# 			if ch in skill:         # 스킬트리 중에 skill이 있다면 s에 추가
# 				s += ch

# 		if skill[:len(s)] == s:     # 만든 s를 기준으로 skill과 같다면 count += 1
# 			count += 1

# 	return count

# def solution(skill, skill_trees):
# 	answer = 0
# 	for tree in skill_trees:
# 		s = ''
# 		for i in tree:
# 			if i in skill:
# 				s += i
# 		if skill[:len(s)] == s:
# 			answer += 1
# 	return answer
# skill = 'CBD'
# skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# print(solution(skill, skill_trees))


# 3번.
# https://school.programmers.co.kr/learn/courses/30/lessons/1843
