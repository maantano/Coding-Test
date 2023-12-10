# 축구는 평일 오후에 하고 의무 참석도 아니다.
# 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다.
# 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

# 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때,팀에 더해지는 능력치이다.

import sys
n = int(input())
g = []
for i in range(n):
	g.append(list(map(int,input().split())))
min_value = int(1e9)
visit = [ False for _ in range(n)]


def bt(depth,idx):
	global min_value
	if depth == n // 2:
		power1,power2 = 0,0
		for i in range(n):
			for j in range(n):
				if visit[i] and visit[j]:
					power1+=g[i][j]
				elif not visit[i] and not visit[j]:
					power2 += g[i][j]
		min_value = min(min_value,abs(power1-power2))
		return
	for i in range(idx,n):
		if not visit[i]:
			visit[i] = True
			bt(depth+1,i+1)
			visit[i] = False
bt(0,0)
print(min_value)






import sys
from itertools import combinations
n = int(sys.stdin.readline())

g = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
members = list(range(n))

min_value = sys.maxsize

for r1 in combinations(members,n//2):
	start,link = 0,0
	r2 = list(set(members) - set(r1))

	for r in combinations(r1,2):
		start += g[r[0]][r[1]]
		start += g[r[1]][r[0]]
	for r in combinations(r2,2):
		link += g[r[0]][r[1]]
		link += g[r[1]][r[0]]
	min_value = min(min_value, abs(start-link))
print(min_value)
