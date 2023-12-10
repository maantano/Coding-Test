import sys
input = sys.stdin.readline

k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]

# k = 4
# m = 3
# score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
def solution(k, m, score):
	answer = 0
	score.sort(reverse=True)
	t = len(score) // m
	for i in range(t):
		answer +=  min(score[i*m:i*m+m]) * m
	return answer

solution(k, m, score)
