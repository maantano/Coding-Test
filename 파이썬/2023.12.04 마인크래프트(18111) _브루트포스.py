
import sys
input = sys.stdin.readline


n,m,b = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]

answer = int(1e9)
idx = 0

for floor in range(257):
	exceed_block,lack_block = 0,0

	for i in range(n):
		for j in range(m):
			if g[i][j] > floor:
				exceed_block += g[i][j] - floor
			else:
				lack_block += floor - g[i][j]
	if exceed_block + b < lack_block:
		continue
	if exceed_block * 2 + lack_block <= answer:
		answer = exceed_block * 2 + lack_block
		idx = floor
print(answer,idx)



# import sys
# N, M, B = map(int,input().split())
# block = []
# for _ in range(N):
# 	block.append([int(x) for x in sys.stdin.readline().rstrip().split()])
# ans = int(1e9)
# glevel = 0

# for i in range(257): #땅 높이
# 	use_block = 0
# 	take_block = 0
# 	for x in range(N):
# 		for y in range(M):
# 			if block[x][y] > i:
# 				take_block += block[x][y] - i
# 			else:
# 				use_block += i - block[x][y]

# 	if use_block > take_block + B:
# 		continue

# 	count = take_block * 2 + use_block

# 	if count <= ans:
# 		ans = count
# 		glevel = i

# print(ans, glevel)
