n = int(input())
row = [0] * n
result = 0
def chk(x):
	for i in range(x):
		if row[i] == row[x] or (abs(x-i) == abs(row[x]-row[i])):
			return False
	return True



def nQ(x):
	global result
	if x == n:
		result +=1
		return
	else:
		for i in range(n):
			row[x] = i
			if chk(x):
				nQ(x+1)
nQ(0)
print(result)
