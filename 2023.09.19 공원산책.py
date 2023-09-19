park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
result = [2,1]

# def solution(park, routes):
# 	answer = []
# 	h = len(park)
# 	w = len(park[0])
# 	x,y = 0,0

# 	nav = {
# 		'S': [1,0],
# 		'N':[-1,0],
# 		'W': [0,-1],
# 		'E':[0,1]
# 	}
# 	for i in range(h):
# 		for j in range(w):
# 			if park[i][j] == "S":
# 				x = i
# 				y = j


# 	for route in routes:
# 		direction, distance = route.split()
# 		distance = int(distance)
# 		flag = 0
# 		step_x = x
# 		step_y = y
# 		for i in range(1,distance+1):
# 			step_x += nav[direction][0]
# 			step_y += nav[direction][1]
# 			if step_x >= h or step_x <= -1 or step_y >= w or step_y <= -1 or park[step_x][step_y] == 'X':
# 				flag = 1
# 				break
# 		if(flag == 0):
# 			x += nav[direction][0] * distance
# 			y += nav[direction][1] * distance
# 	answer = [x,y]
# 	return answer

#  더 간결 코드
def solution(park, routes):
    w, h = len(park), len(park[0])
    for i,v in enumerate(park):
        if 'S' in v:
            y,x=i,v.find("S")

    navi = {'E':[1, 0], 'W': [-1, 0], 'S': [0, 1], 'N': [0, -1]}
    for go in routes:
        op, l = go.split(' ')
        l=int(l)
        dir_x, dir_y = navi[op]
        block=False
        if not ((x+dir_x * l) in range(0, h) and (y + dir_y*l) in range(0, w)):
            continue
        for l2 in range(1, l + 1):
            if park[y+dir_y * l2][x+dir_x * l2] == 'X':
                block=True
        if not block:
            x += dir_x * l
            y += dir_y * l

    return [y,x]


solution(park, routes)
