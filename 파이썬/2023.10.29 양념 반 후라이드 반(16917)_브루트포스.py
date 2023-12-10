# import sys
# input = sys.stdin.readline


# a,b,c,x,y = map(int,input().split(' '))

# answer = 0
# while True:
# 	if x == 0 and y == 0:
# 		break

# 	if x * y != 0:
# 		answer += min(a+b,c*2)
# 		x-=1
# 		y-=1
# 	else:
# 		if x == 0:
# 			answer += min(b,c*2)
# 			y-=1
# 		else:
# 			answer += min(a,c*2)
# 			x-=1
# print(answer)



A, B, C, X, Y = map(int, input().split())
if A+B < C*2:
	print(A*X + B*Y)
else:
	m=min(X,Y)
	print(C*m*2 + min(C*2, A) * max(0, X-m) + min(C*2, B) * max(0, Y-m))
