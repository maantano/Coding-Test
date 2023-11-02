# import sys
# from collections import deque

# for i in range(3):
# 	chk = int(input().rstrip())
# 	q = deque([chk])
# 	visited = {}


# 	while True:
# 		x = q.popleft()

# 		if len(str(x)) * '1' in visited.keys():
# 			print(len(str(x)))
# 			break

# 		if x*2 not in visited.keys():
# 			q.append(x*2)
# 			visited[x*2] = x*2
# 		if x*3 not in visited.keys():
# 			q.append(x*3)
# 			visited[x*3] = x*3
# 		if x*5 not in visited.keys():
# 			q.append(x*5)
# 			visited[x*5] = x*5
# 		if x*7 not in visited.keys():
# 			q.append(x*7)
# 			visited[x*7] = x*7
# 		print(visited)
# 		print(q)


# for i in range(3):
# 	chk = int(input().rstrip())
# 	i = 1
# 	while True:
# 		if str(chk * i) == len(str(chk * i)) * '1':
# 			print(len(str(chk*i)))
# 			break
# 		i+=1



# for i in range(3):
# 	chk = int(input().rstrip())
# 	i = 1
# 	while True:
# 		if str(chk * i) == len(str(chk * i)) * '1':
# 			print(len(str(chk*i)))
# 			break
# 		i+=1


while True:
	try:
		chk = int(input().rstrip())
	except:
		break
	i = 1
	while True:
		if int('1'*i) % chk == 0:
			print(len('1'*i))
			break
		i+=1
