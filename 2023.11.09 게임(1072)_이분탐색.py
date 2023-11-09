
# X = 횟수
# Y = 이긴 횟수
# Z  = print(int(47 // (53 * 0.01)))


# X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
x,y = map(int,input().split())
z = (y*100) // x

if z > 98:
	print(-1)
	exit()
start = 0
end = x

while start < end:
	mid = (start+end) // 2

	if (y+mid) * 100 // (x+mid) != z:
		end = mid
	else:
		start = mid + 1
mid = (start + end) // 2
print(mid)





