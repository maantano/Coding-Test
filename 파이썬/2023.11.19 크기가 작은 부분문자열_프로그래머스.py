import sys
input = sys.stdin.readline

t = "3141592"
p = '271'

def solution(t,p):
	answer = 0
	for i in range(len(t)-len(p)+1):
		if int(t[i:i+len(p)]) <= int(p):
			answer+=1
	return answer
solution(t,p)
