
import sys
input = sys.stdin.readline

n,m = map(int,input().split(' '))
board = [list(map(str,input().rstrip())) for _ in range(n)]
result = []

for i in range(n-7):
	for j in range(m-7):
		black = 0
		white = 0

		for a in range(i,i+8):
			for b in range(j,j+8):
				if (a+b) % 2 == 0:
					if board[a][b] != 'B':
						white +=1
					else:
						black+=1
				else:
					if board[a][b] != 'W':
						white +=1
					else:
						black +=1
		result.append(white)
		result.append(black)
print(min(result))




# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split(' '))
# arr = [list(map(str,input().rstrip())) for _ in range(n)]
# tmp = 0
# answer = []
# for i in range(n):
# 	minTmp = 50
# 	for j in range(m-7):
# 		minTmp = min(abs(arr[i][j:j+8].count('B')-4), minTmp)
# 	answer.append(minTmp)


# cnt = 50
# for i in range(len(answer)-8):
# 	cnt=  min(sum(answer[i:i+8]),cnt)
# if cnt == 50:
# 	print(0)
# else:
# 	print(cnt)
