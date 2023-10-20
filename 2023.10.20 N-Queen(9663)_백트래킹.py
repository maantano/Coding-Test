


# n = int(input())
# row = [0]*n
# result = 0

# def chkQ(x):
# 	for i in range(x):
# 		if row[i] == row[x] or (abs(x-i) == abs(row[x]-row[i])):
# 			return False
# 	return True

# def nQ(x):
# 	global result
# 	if x == n:
# 		result +=1
# 	else:
# 		for i in range(n):
# 			row[x] = i
# 			if chkQ(x):
# 				nQ(x+1)

# nQ(0)
# print(result)


import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * n
def chk(n):
	for i in range(n):
		if arr[n] == arr[i] or (abs(n-i)) == abs(arr[n]-arr[i]):
			return False
	return True

result = 0
def nQ(x):
	global result
	if x == n:
		result+=1
	else:
		for i in range(n):
			arr[x] = i
			if chk(x):
				nQ(x+1)
nQ(0)
print(result)
