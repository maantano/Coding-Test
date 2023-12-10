import sys
input = sys.stdin.readline


# s = 'banana'
s = 'foobar'

def solution(s):
	visited = [-1] * len(s)
	d = {}
	for i in range(len(s)):
		if s[i] not in d:
			d[s[i]] = i+1
		else:
			visited[i] = i+1-d[s[i]]
			d[s[i]] = i+1
	return visited


solution(s)
