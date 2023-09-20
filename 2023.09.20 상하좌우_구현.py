# n = 5
# arr = ['R','R','R','U','D','D']

# 내 풀이
n = int(input())
arr = map(str,input().split())


path = {
	'L':[0,-1],
	'R':[0,1],
	'U':[-1,0],
	'D':[1,0]
}
start_x = 1
start_y = 1
for i in arr:
	x,y= path[i]
	if not ((x+start_x) in range(1, n+1) and ((y+start_y) in range(1, n+1))):
		continue
	start_x +=x
	start_y +=y
print(start_x,start_y)


# 책 풀이

n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_types = ['L','R','U','D']

for plan in plans:
	for i in range(len(move_types)):
		if plan == move_types[i]:
			nx = x + dx[i]
			ny = y + dy[i]
	if nx < 1 or ny < 1 or nx >n or ny >n:
		continue
	x,y = nx,ny
print(x,y)
