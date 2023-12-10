


# for i in range(n,m):
# 		if i == 1:
# 			continue
# 		for j in range(2,int(i**(1/2))+1):
# 			if i % j == 0:
# 				break
# 			else:
# 				print(i)

def isPrime(num):
	if num == 1:
		return False
	else:
		for i in range(2,int(num ** (1/2))+1):
			if num % i == 0:
				return False
		return True

n,m = map(int,input().split(' '))
for i in range(n,m+1):
	if isPrime(i):
		print(i)





# def getMyDivisor(n):
# 	divisorsList = []
# 	for i in range(1, int(n**(1/2)) + 1):
# 		if (n % i == 0):
# 			divisorsList.append(i)
# 			if (i**2) != n:
# 				divisorsList.append(n // i)
# 	# divisorsList.sort()
# 	return (divisorsList)

# def getDivision(n):
# 	for i in range(n,m+1):
# 		if i == 1:
# 			continue
# 		for j in range(2,int(i**(1/2))+1):
# 			if i % j == 0:
# 				break
# 			else:
# 				return i
