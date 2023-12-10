
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
result = [0,2,2,0,1,0,0,0,0,0,0]
# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]
# result = [-1]

# from itertools import combinations_with_replacement
# def solution(n, info):
# 	answer = [-1]
# 	result_list = []
# 	score_num = [0,1,2,3,4,5,6,7,8,9,10]
# 	mx_board = [-1]
# 	mx_gap = -1
# 	for score_list in list(combinations_with_replacement(score_num, n)):
# 		lion = 0
# 		appeach = 0
# 		score_board = [0 for _ in range(11)]
# 		for score in score_list:
# 			score_board[10 - score] += 1

# 		for i in range(11):
# 			if score_board[i] == 0 and info[i] == 0:
# 				continue
# 			if score_board[i] > info[i]:
# 				lion += (10 - i)
# 			else:
# 				appeach += (10 - i)

# 		if lion > appeach:
# 			gap = lion - appeach
# 			if gap > mx_gap:
# 				mx_gap = gap
# 				mx_board = score_board

# 	return mx_board



def solution(n, info):
	# 어피치의 총 점수 계산
	apeach = sum([10-i for i in range(10) if info[i]])
	# 과녁의 각 점수별 실질적으로 얻어지는 점수
	score = [(10-i)*2 if info[i] else 10-i for i in range(10)]



	# BFS를 위한 queue. 10점을 쏘지 않은 경우 기본 추가
	queue = [[0]]
	answer = []
	# 10점을 쏠 수 있는 경우, 쏜 경우를 queue에 추가
	if n >= info[0]+1:
		queue.append([info[0]+1])

	while queue:
		recent = queue.pop(0)
		# 주어진 화살을 다 쐈거나, 10~1점까지 다 쏜 경우
		if sum(recent) == n or len(recent) == 10:
			new = sum([score[i] for i in range(len(recent)) if recent[i]])
			old = sum([score[i] for i in range(len(answer)) if answer[i]])
			# apeach보다 많은 점수를, 그리고 기존 answer 이상의 점수를 얻었다면 update
			if new > apeach and new >= old:
				answer = recent
		# 아직 덜 쐈는데, 이번 점수에 (어피치+1)을 쏠 수 있다면
		elif sum(recent)+info[len(recent)]+1 <= n:
			# 쏜 경우, 안 쏜 경우 모두 queue에 append
			queue.append(recent + [info[len(recent)]+1])
			queue.append(recent + [0])
		# 아직 덜 쐈는데, 쏠 화살이 안 남아있다면, 안 쏜 경우만 append
		else :
			queue.append(recent + [0])
	# apeach보다 많은 점수를 낼 수 없다면, [-1] return
	if not answer:
		return [-1]
	# 그렇지 않다면, [answer + 남은 점수 안쏘고 + 0점에 다 쏘기] return
	return answer + [0]*(10 - len(answer)) + [n-sum(answer)]


def solution(n, info):
	answer = []
	ryan = [0]*11
	diff = 0

	# m: 쏜 화살 수, idx: 현재 탐색하는 과녁 번호
	def dfs(m, idx):
		nonlocal answer, diff, ryan

		if m == n:
			r, a = 0, 0

			for j in range(11):
				# 둘다 1발은 쐈고,
				# 라이언이 한발이라도 더 쐈다면 라이언 + 아니면 어피치 +
				if ryan[j] > info[j]:
					r += 10-j
				elif 0 != info[j] and ryan[j] <= info[j]:
					a += 10-j

			# 라이언이 점수가 더 높을 때
			if r > a:
				# 격차가 더 크다면 바로 갱신
				if diff < r - a:
					diff = r - a
					answer = ryan[:]

				# 격차가 같다면 낮은 점수를 더 많이 쏜 걸로 갱신
				elif diff == r - a:
					for i in range(10, -1, -1):
						if ryan[i] < answer[i]:
							break
						if ryan[i] > answer[i]:
							answer = ryan[:]
							break
			return

		for i in range(idx, 11):
			ryan[i] += 1
			dfs(m+1, i)
			ryan[i] -= 1


	dfs(0, 0)

	return answer if answer else [-1]

solution(n, info)
# from collections import deque

# def dfs(i,n,chk):
# 	if n <=0:
# 		return chk
# 	chk += (10 - i)
# 	return chk

# def solution(n, info):
# 	visited = [0] * 10
# 	# q = deque([(0,n)])
# 	answer = []
# 	chk = 0
# 	for i in range(len(info)):
# 		if not visited[i]:
# 			visited[i] = 1
# 			dfs(i,n-info[i],chk)
# 			visited[i] = 0

# 	return answer


