from collections import deque
import sys
input = sys.stdin.readline

s = int(input().rstrip())
visited = {}


def bfs():
	q = deque([(1,0)])
	visited[(1,0)] = 0
	while q:
		now,clip = q.popleft()
		if now == s:
			print(visited[(now,clip)])
			break
		if (now,now) not in  visited.keys():
			visited[(now,now)] = visited[(now,clip)] + 1
			q.append((now,now))
		if (now+clip,clip) not in visited.keys():
			visited[(now+clip,clip)] = visited[(now,clip)]+1
			q.append((now+clip,clip))
		if (now - 1,clip) not in visited.keys():
			visited[(now-1,clip)] = visited[(now,clip)] + 1
			q.append((now-1,clip))

bfs()

