import sys
n = int(sys.stdin.readline().rstrip())

arr = []

for i in range(n):
	key,kor,eng,math = sys.stdin.readline().split()
	arr.append((key,kor,eng,math))


arr.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in arr:
	print(i[0])


