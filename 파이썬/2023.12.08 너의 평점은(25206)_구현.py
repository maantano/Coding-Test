# import sys
# input = sys.stdin.readline

# s = set()
# total = 0
# chk = 0
# for i in range(20):
# 	a,b,c= input().split()
# 	chk+=int(b)

# 	if c == 'P':
# 		continue
# 	else:
# 		if c == 'A+':
# 			total+= round((float(b) *4.5),4)
# 		elif c == 'A0':
# 			total+= round((float(b) *4.0),4)
# 		elif c == 'float(b)+':
# 			total+= round((float(b) *3.5),4)
# 		elif c == 'float(b)0':
# 			total+= round((float(b) *3.0),4)
# 		elif c == 'C+':
# 			total+= round((float(b) *2.5),4)
# 		elif c == 'C0':
# 			total+= round((float(b) *2.0),4)
# 		elif c == 'D+':
# 			total+= round((float(b) *1.5),4)
# 		elif c == 'D0':
# 			total+= round((float(b) *1.0),4)
# 		else:
# 			total+= float(b) * 0

# print(total//chk)

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
result = 0
for _ in range(20) :
	s, p, g = input().split()
	p = float(p)
	if g != 'P' :
		total += p
		result += p * grade[rating.index(g)]

print('%.6f' % (result / total))
