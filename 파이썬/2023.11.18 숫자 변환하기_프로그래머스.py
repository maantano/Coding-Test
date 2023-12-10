import sys
input = sys.stdin.readline

from collections import deque

def solution(x, y, n):
	visited = [0] * 1000001

	q = deque()
	q.append((x, 0))
	visited[x] = 1
	while q:
		num, cnt = q.popleft()
		if num == y:
			return cnt
		for next_num in (num + n, num * 2, num * 3):
			if next_num <= y and not visited[next_num]:
				visited[next_num] = 1
				q.append((next_num, cnt + 1))

	return -1



def solution(x, y, n):
	answer = 0
	s = set()
	s.add(x)

	while s:
		if y in s:
			return answer
		nx = set()

		for i in s:
			if i+n <= y:
				nx.add(i+n)

			if i*2 <= y:
				nx.add(i*2)

			if i*3 <= y:
				nx.add(i*3)

		s = nx
		answer += 1

	return -1



def solution(x, y, n):
	answer = 0
	q=[]
	q.append((y,0))
	while q:
		tmp=q.pop(0)
		if tmp[0]==x:
			return tmp[1]
		if tmp[0]>x:
			if tmp[0]%3==0:
				q.append((tmp[0]/3,tmp[1]+1))
			if tmp[0]%2==0:
				q.append((tmp[0]/2,tmp[1]+1))
			q.append((tmp[0]-n,tmp[1]+1))

	return -1
