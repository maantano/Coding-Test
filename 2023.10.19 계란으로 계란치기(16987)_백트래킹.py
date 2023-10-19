import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

cnt = 0

visited = [0]*(n+1)
def bt(idx):
	global cnt
	if idx == n or n == 1:
		print(cnt)
		exit()
	for i in range(n-1):
		for j in range(i+1,n):
			x,y = arr[i]
			x2,y2 = arr[j]
			first = x-y2
			second = x2 -y
			if x == 0:
				continue
			if not visited[i]:
				if first < 0 and second <0:
					cnt+2
					arr[i] = [0,0]
					arr[j] = [0,0]
					visited[i] =1
					visited[j] =1
				elif x-y2 <0:
					cnt+=1
					arr[i] = [0,0]
					visited[i] =1
				elif x-y2 >0 and x2-y < 0:
					arr[j] = [0,0]
					visited[j] =1
			bt(idx+1)
bt(0)











