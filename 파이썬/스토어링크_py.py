# 	# n개의 집이 원형으로 세워져 있는 마을이 있다.
# 	# 각 집에는 1부터 n 까지 순서대로 번호가 붙어있다. 이 마을에서 바로 옆에 위치한 집으로 이동하는데, 1만큼의 단위 시간이 걸립니다.
# 	# 또 집과 집 사이를 오가기 위해서는 중간에 위치한 집들을 반드시 거쳐서 이동해야 합니다. 다음은 n =5 인 경우의 예시입니다.

# 	# 1번 집에서 2번집, 또는 5번집으로 이동하는데는 1의 시간이 소요됩니다. 또 1번 집에서 3번집으로 이동하기 위해서는 시계방향으로 2번 집을 거쳐 가거나, 혹은 반시계 방향으로 5번과 4번 집을 거쳐서 이동해야합니다.
# 	# 따라서 1번 집에서 3번집으로 이동하는 데는 2또는 3의 시간이 소요됩니다.

# 	# 이 마을을 방문한 한 여행자가 현재 1번 집 앞에 있습니다. 이 여행자는 이 마을에 있는 모든 집을 미리 정해진 순서대로 방문하려고 합니다.
# 	# 예시 1번입니다. 예를들어 예시에서 여행자가 미리 방문하기로 한 집의 순서가 [1,2,3,4,5] 라면 1번 집부터 시계방향으로 각 집을 방문하면 총 4의 단위 시간에 모든 집을 방문 할 수 있습니다.

# 	# 예시 2번입니다.
# 	# 만약 미리 방문하기로 한 집의 순서가 [3,5,4,1,2] 라면 다음과 같은 순서로 모든 집을 방문 할 수 있습니다.

# 	# 1. 여행자는 처음에 1번 집 앞에 있으며, 시계 방향으로 2번 집을 거쳐 3번 집으로 이동하면 2의 시간이 소요됩니다.
# 	# 2. 3번 집에서 시계방향으로 4번 집을 거쳐 5번 집으로 이동하면 2의 시간이 소요됩니다.
# 	# 3. 5번 집에서 반시계 방향으로 4번 집으로 이동하면 1의 시간이 소요됩니다.
# 	# 4. 4번 집에서 시계방향으로 5번 집을 거쳐 1번 집으로 이동하면 2의 시간이 소요 됩니다.
# 	# 5. 1번 집에서 시계방향으로 2번 집으로 이동하면 1의 시간이 소요됩니다.


# 	# 위 방법대로 이동하면 총 8의 시간이 소요되며, 이때가 모든 집을 미리 정해진 순서대로 방문하는데 걸리는 시간의 최솟값이 됩니다.
# 	# 마을에 원형으로 세워져 있는 집의 개수가 n과 여행자가 모든 집을 방문하기 위해 미리 정해든 순서가 들어있는 배열 sequence 가 매개변수로 주어질 때,
# 	# 여행자가 미리 정해둔 순서대로 모든 집을 방문하는데 필요한 시간의 최솟값을 return 하도록 solution 함수를 완성하세요.

# 	# 문제 1. n = 5, sequence = [1,2,3,4,5]
# 	# 문제 2. n = 5, sequence = [3,5,4,1,2]
# 	# def solution(n, sequence):

# 	# def solution(n, sequence):
# 	#     answer = 0

# 	#     if sequence[0] != 1:
# 	#         # sequence[0]이 1이 아닌 경우, 해당 집에서부터 1번 집까지의 거리를 더함
# 	#         diff = abs(sequence[0] - 1)
# 	#         answer += min(diff, n - diff)

# 	#     for i in range(len(sequence) - 1):
# 	#         diff = abs(sequence[i] - sequence[i + 1])
# 	#         answer += min(diff, n - diff)

# 	#     return answer

# 	# # 예시 1
# 	# n1 = 5
# 	# sequence1 = [1, 2, 3, 4, 5]
# 	# result1 = solution(n1, sequence1)
# 	# print(result1)  # 출력값: 4

# 	# # 예시 2
# 	# n2 = 5
# 	# sequence2 = [3, 5, 4, 1, 2]
# 	# result2 = solution(n2, sequence2)
# 	# print(result2)  # 출력값: 8


# 	# ================================================================================================================================



# 	# 여러 수의 덧셈('+'), 뺄셈('-'), 곱셈('*'),으로 이루어진 식에 괄호 한 쌍을 올바르게 삽입하여 식을 계산한 결과가 최대가 되도록 하려고 합니다.
# 	# 예를 들어 2-1*5-4*3+2 라는 식을 계산하면 -13입니다. 여기에 괄호를 한쌍 추가하여 2-1*(5-4)*3+2로 만든다면 계산 결과는 1이 됩니다. 하지만 만약
# 	# 2-(1*5-4*3)+2로 만든다면 결과는 11이 되어 최대가 됩니다.
# 	# 덧셈, 뺼셈과 곱셉으로 이루어진 식 expression이 매개변수로 주어질 때, 괄호 한쌍을 올바르게 삽입하여 계산한 결과의 최대값을 return 하는 solution 함수를 만드세요.

# 	# 문제 1. expression = "2-1x5-4x3+2", result :11
# 	# 문제 2. expression = "2x3-1", result : 5


# 	# from itertools import permutations

# 	# def calculate(a, b, operator):
# 	#     if operator == '+':
# 	#         return a + b
# 	#     elif operator == '-':
# 	#         return a - b
# 	#     elif operator == '*':
# 	#         return a * b

# 	# def solution(expression):
# 	#     answer = 0

# 	#     # 연산자 우선순위의 모든 가능한 순열 생성
# 	#     priorities = set(permutations(['+', '-', '*']))

# 	#     for priority in priorities:
# 	#         temp_expression = expression
# 	#         for operator in priority:
# 	#             temp_expression = temp_expression.replace(operator, ' ' + operator + ' ')

# 	#         # 연산자 우선순위에 따라 계산
# 	#         values = list(map(str.strip, temp_expression.split()))
# 	#         stack = []
# 	#         operators = []

# 	#         for token in values:
# 	#             if token.isdigit():
# 	#                 stack.append(int(token))
# 	#             else:
# 	#                 while operators and priority.index(operators[-1]) >= priority.index(token):
# 	#                     stack.append(calculate(stack.pop(-2), stack.pop(), operators.pop()))
# 	#                 operators.append(token)

# 	#         while operators:
# 	#             stack.append(calculate(stack.pop(-2), stack.pop(), operators.pop()))

# 	#         # 최대값 업데이트
# 	#         answer = max(answer, abs(stack[0]))

# 	#     return answer

# 	# # 테스트 케이스
# 	# print(solution("2-1*5-4*3+2"))  # 결과: 11
# 	# print(solution("2*3-1"))  # 결과: 5
# 	# expression = "2-1x5-4x3+2"
# 	# result :11

# 	# def solution(expression):
# 	# 	# unit = ['+','-','*']
# 	# 	for i in expression:
# 	# 		if i.isdigit():








# 	# 	answer = 0;
# 	# 	return answer;

# exp = '2x3-1'

# # eval()
# import sys
# # N = int(sys.stdin.readline())

# # words = ['2','*','3','-','1']

# # words = list(sys.stdin.readline().rstrip())
# # mv = float('-inf')

# # def dfs(i, value):
# # 	global mv
# # 	if N == i:
# # 		mv = max(mv, int(value))
# # 		return
# # 	# 괄호 사용 o
# # 	if i+4 <= N:
# # 		dfs(i+4, str(eval(''.join([value, words[i]] + [str(eval(''.join(words[i+1:i+4])))]))))
# # 	# 괄호 사용 x
# # 	if i+2 <= N:
# # 		dfs(i+2, str(eval(''.join([value] + words[i:i+2]))))
# # dfs(1, words[0])
# # print(mv)


# # s = input()
# # s = ['2','-','1','x','5','-','4','x','3','+','2']




# import sys
# # N = int(sys.stdin.readline())
# # words = list(sys.stdin.readline().rstrip())
# # mv = float('-inf')

# # def dfs(i, value):
# #     global mv
# #     if N == i:
# #         mv = max(mv, int(value))
# #         return
# #     if i+4 <= N:
# #         dfs(i+4, str(eval(''.join([value, words[i]] + [str(eval(''.join(words[i+1:i+4])))]))))
# #     if i+2 <= N:
# #         dfs(i+2, str(eval(''.join([value] + words[i:i+2]))))
# # dfs(1, words[0])
# # print(mv)
# # import sys

# # exp = "2x3-1"
# # answer = 0
# # def solution(idx,l):
# # 	global answer
# # 	if idx == len(exp):
# # 		return answer

# 	#



# card = ["ABACDEFG", "NOPQRSTU", "HIJKLKMM"]
# word = ["GPQM", "GPMZ", "EFU", "MMNA"]
# # arr = [list(i) for i in card]
# # arr = [
# # 	['A', 'B', 'A', 'C', 'D', 'E', 'F', 'G'],
# # 	['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
# # 	['H', 'I', 'J', 'K', 'L', 'K', 'M', 'M']
# # 	   ]
# # for i in range(len(card)):
# # 	arr.append(list(card[i]))
# # print(arr)

# # card = ["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"]
# # word = ["AAAKKKKKMMMMM", "ABCDKJ"]





# import sys
# input = sys.stdin.readline
# answer = []

# arr = [list(i) for i in card]
# def chkWord(word):
# 	visited = [[0] * (len(word)) for _ in range(len(card))]
# 	visitedRow = [0] * len(card)
# 	d = {}
# 	for i in range(len(card)):
# 		for j in range(len(card[i])):
# 			if card[i][j] not in d:
# 				d[card[i][j]] = 1
# 			else:
# 				d[card[i][j]] += 1

# 	for i in range(len(word)):
# 		for j in range(len(arr)):

# 			if word[i] not in d.keys():
# 				return

# 			if word[i] in arr[j]:
# 				visited[j][i] = 1
# 				visitedRow[j] = 1
# 				d[word[i]] -=1
# 				continue
# 	if 0 in visited or 0 in visitedRow or -1 in d.values():
# 		return

# 	answer.append(word)


# for i in word:
# 	chkWord(i)
# if not len(answer):
# 	print(['-1'])
# else:
# 	print(answer)





import sys
N = int(sys.stdin.readline())
cal = list(sys.stdin.readline().strip())
result = -1*2**31 # 최솟값

def calculate(a, op, b):
	if op=='+':
		num = a + b
	elif op=='*':
		num = a * b
	elif op == '-':
		num = a - b
	return num

def dfs(index, value):
	global result

	if index == N - 1:
		result = max(result, value)
		return

	if index + 2 < N:
		next_value = calculate(value, cal[index + 1], int(cal[index + 2]))
		dfs(index + 2, next_value)

	if index + 4 < N:
		next_next_value = calculate(int(cal[index+2]), cal[index+3], int(cal[index+4]))
		next_value = calculate(value, cal[index + 1], next_next_value)
		dfs(index + 4, next_value)

dfs(0, int(cal[0]))
print(result)

