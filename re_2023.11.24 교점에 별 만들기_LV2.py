line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]

def meetPoint(l1,l2):
	x1,y1,c1= l1
	x2,y2,c2= l2

	if x1*y2 == x2*y1:
		return
	x = (y1*c2 - y2*c1) / (x1*y2 - x2*y1)
	y = (x2*c1 - x1*c2) / (x1*y2 - x2*y1)

	if x == int(x) and y == int(y):
		return [int(x),int(y)]

from itertools import combinations

def solution(lines):
	points = []
	for l1,l2 in combinations(lines,2):
		point = meetPoint(l1,l2)
		if point: points.append(point)
	w1, w2 = min(points, key = lambda x : x[0])[0], max(points, key = lambda x : x[0])[0] + 1
	h1, h2 = min(points, key = lambda x : x[1])[1], max(points, key = lambda x : x[1])[1] + 1
	answer = [['.'] * (w2-w1) for _ in range(h2-h1)]

	for x ,y in points:
		answer[y-h1][x-w1] = '*'
	answer.reverse()

	return [''.join(a) for a in answer]

print(solution(line))
