import sys
input = sys.stdin.readline

d = {' ': [0,0,0,0,0,0,0],'0':[1,1,1,0,1,1,1],'1':[0,0,1,0,0,1,0],'2':[1,0,1,1,1,0,1],'3':[1,0,1,1,0,1,1],'4':[0,1,1,1,0,1,0],'5':[1,1,0,1,0,1,1],'6':[1,1,0,1,1,1,1],'7':[1,1,1,0,0,1,0],'8':[1,1,1,1,1,1,1],'9':[1,1,1,1,0,1,1]}
t=int(input())
for k in range(t):
	a,b= input().split()
	a=(5-len(a))*' '+a
	b=(5-len(b))*' '+b

	total=0
	for i in range(5):
		for j in range(7):
			total += (d[a[i]][j] != d[b[i]][j])

	print(total)
# t = int(input())
# chk = [[0]*7 for i in range(5)]
# def convert(x,y):
# 	arrX = []
# 	arrY = []
# 	for i in range(len(x)):
# 		arrX.append(d[x[i]])
# 		arrY.append(d[y[i]])
# 	return arrX,arrY


# for i in range(t):
# 	x,y = map(str,input().split())
# 	xL = list(map(int,x))
# 	yL = list(map(int,y))
# 	if len(xL) > len(yL):
# 		yL = [0]*(len(xL)-len(yL)) + yL
# 	elif len(yL) > len(xL):
# 		xL = [0]*(len(yL)-len(xL))+xL
# 	l1,l2= convert(xL,yL)

# 	cnt = 0
# 	print(l1)
# 	print(l2)
# 	for i in range(len(l1)):
# 		for j in range(len(l1[0])):
# 			if l1[i][j] != l2[i][j]:
# 				cnt+=1
# 	print(cnt)





# # 	if len(xL) > len(yL)




# z = [ 1,
# 	 1,1,
# 	  0,
# 	 1,1,
# 	  1
# 	]

# a = [ 0,
# 	 0,1,
# 	  0,
# 	 0,1,
# 	  0
# 	]
# b = [ 1,
# 	 0,1,
# 	  1,
# 	 1,0,
# 	  1
# 	]

# c = [ 1,
# 	 0,1,
# 	  1,
# 	 0,1,
# 	  1
# 	]

# d = [ 0,
# 	 1,1,
# 	  1,
# 	 0,1,
# 	  0
# 	]
# f = [ 1,
# 	 1,0,
# 	  1,
# 	 0,1,
# 	  1
# 	]
# g = [ 1,
# 	 1,0,
# 	  1,
# 	 1,1,
# 	  1
# 	]
# h = [ 1,
# 	 1,1,
# 	  0,
# 	 0,1,
# 	  0
# 	]
# i = [ 1,
# 	 1,1,
# 	  1,
# 	 1,1,
# 	  1
# 	]
# j = [ 1,
# 	 1,1,
# 	  1,
# 	 0,1,
# 	  1
# 	]
