# # import sys
# # input = sys.stdin.readline

# # m3 = int(input())
# # answer = row = col = 0

# # for i in range(6):
# # 	path,length = map(int,input().split())

# # 	print(path,length)
# # 	if path == 3 or path == 4:
# # 		row = length
# # 	else:
# # 		col = length
# # 	print('row,col ===>',row,col)
# # 	if not row and not col:
# # 		answer += row*col
# # 		row = col = 0
# # print(answer)





# import sys
# input = sys.stdin.readline

# m3 = int(input())
# answer = row = col = 0
# sn = []
# ew = []
# for _ in range(6):
# 	path,length = map(int,input().split())
# 	if path == 3 or path == 4:
# 		sn.append((path,length))
# 	else:
# 		ew.append((path,length))
# sn.sort()
# ew.sort()
# total = sn[-1][1] * ew[-1][1]
# print(total)
# print(sn[-2][1] * ew[-2][1])

# # for i in range(len(sn)):
# # 	snP,snL = sn[i]
# # 	ewP,ewL = ew[i]
# # 	answer += (snL * ewL)

# 	# if path == 3 or path == 4:
# 	# 	row = length
# 	# else:
# 	# 	col = length
# 	# if not row and not col:
# 	# 	answer += row*col
# 	# 	row = col = 0
# # print()
# # print((total-answer)  * m3 )







import sys
K = int(sys.stdin.readline())

height = []
width = []
total = []
for i in range(6):
	dir, length = map(int, sys.stdin.readline().split())
	if dir == 1 or dir ==2:
		width.append(length)
		total.append(length)
	else:
		height.append(length)
		total.append(length)
bigbox = max(height) * max(width)
maxhidx = total.index(max(height))
maxwidx = total.index(max(width))

small1 = abs(total[maxhidx-1] - total[(maxhidx-5 if maxhidx == 5 else maxhidx +1)])
small2 = abs(total[maxwidx-1] - total[(maxwidx-5 if maxwidx == 5 else maxwidx +1)])

print((bigbox - (small1 * small2))*K)
