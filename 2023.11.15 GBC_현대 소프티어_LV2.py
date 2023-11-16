import sys
input = sys.stdin.readline

n,m = map(int,input().split())

limit = [0]*101
now = 1


for _ in range(n):
	section,speed = map(int,input().split())
	for i in range(now,now+section):
		limit[i] = speed
	now+=section

result = 0
now = 1
for _ in range(m):
	section,speed = map(int,input().split())
	for i in range(now,now+section):
		result = max(result,speed-limit[i])
	now += section
if result >=0:
	print(result)
else:
	print(0)

import sys

N, M = map(int, sys.stdin.readline().split())

N_section = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M_section = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
total = 0
max_diff = []

while True:
	if N_section == [] or M_section == []:
		break

	diff_length = M_section[0][0] - N_section[0][0]

	if diff_length > 0:
		max_diff.append(M_section[0][1] - N_section[0][1])
		N_section.pop(0)
		M_section[0][0] = diff_length

	elif diff_length < 0:
		max_diff.append(M_section[0][1] - N_section[0][1])
		M_section.pop(0)
		N_section[0][0] = -diff_length

	else:
		max_diff.append(M_section[0][1] - N_section[0][1])
		M_section.pop(0)
		N_section.pop(0)

if max(max_diff) >= 0:
	print(max(max_diff))

else:
	print(0)
