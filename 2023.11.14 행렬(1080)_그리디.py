
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

arr = [list(map(int,input().rstrip())) for _ in range(n)]
arr2 = [list(map(int,input().rstrip())) for _ in range(n)]


def chk(i,j):
	for x in range(i,i+3):
		for y in range(j,j+3):
			if arr[x][y] == 0:
				arr[x][y] = 1
			else:
				arr[x][y] = 0

cnt = 0

if (n <3 or m < 3) and arr != arr2:
	cnt = -1

else:
	for r in range(n-2):
		for c in range(m-2):
			if arr[r][c] != arr2[r][c]:
				cnt +=1
				chk(r,c)
if cnt != -1:
	if arr != arr2:
		cnt = -1
print(cnt)

