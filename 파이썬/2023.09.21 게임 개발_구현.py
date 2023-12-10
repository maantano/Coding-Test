
# 내 풀이
x,y = map(int,input().split())
start_x,start_y,way = map(int,input().split())
# x= 4
# y= 4
# start_x=1
# start_y=1
# way = 0
# arr=[[1,1,1,1],
# [1,0,0,1],
# [1,1,0,1],
# [1,1,1,1]
# ]

direction = {
	0 : (-1,0), # 북
	1 : (0,1), # 동
	2 : (1,0), # 남
	3 : (0,-1), # 서
}
d = [[0]* x for _ in range(x)]
d[start_x][start_y] = 1
arr = []
for i in range(x):
	arr.append(list(map(int,input().split())))

def turn_left():
	global way
	way -= 1
	if way == -1:
		way = 3

moveCnt = 1
turnC = 0
while True:
	move_x,move_y = direction[way]
	if d[start_x+move_x][start_y+move_y] == 0 and arr[start_x+move_x][start_y+move_y] == 0:

		start_x += move_x
		start_y += move_y
		d[start_x][start_y] = 1
		moveCnt +=1
		turnC = 0
	else:
		turn_left()
		turnC +=1
	if turnC == 4:
		if arr[start_x - move_x][start_y-move_y] == 0:
			start_x = start_x - move_x
			start_y = start_y-move_y
		else:
			break
		turnC = 0



print('moveCnt ===>',moveCnt)


# 책풀이

# n, m = map(int, input().split())
# d = [[0]*m for _ in range(n)]

# x,y,direction = map(int,input().split())

# d[x][y] = 1
# array = []
# for i in range(n):
# 	array.append(list(map(int,input().split())))
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def turn_left():
# 	global direction
# 	direction -= 1
# 	if direction == -1:
# 		direction = 3


# count = 1
# turn_time = 0

# while True:
# 	turn_left()
# 	nx = x + dx[direction]
# 	ny = y + dy[direction]
# 	if d[nx][ny] == 0 and array[nx][ny] == 0:
# 		d[nx][ny] = 1
# 		x = nx
# 		n = ny
# 		count +=1
# 		turn_time = 0
# 		continue
# 	else:
# 		turn_time +=1

# 	if turn_time == 4:
# 		nx = x - dx[direction]
# 		ny = y - dy[direction]
# 		if array[nx][ny] == 0:
# 			x = nx
# 			y = ny
# 		else:
# 			break
# 		turn_time = 0
