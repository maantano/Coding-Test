# 철수가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고
# 영희가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a

# 영희가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고,
# 철수가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a



# print(gcd(10,17))
# print(gcd(10,20))
# print(if 17 % gcd(10,20) > 0 : 0)

# print(gcd(14,35))
# print(gcd(14,119))
# print(lcm(17,lcm(35,199)))
# print(gcd(17,118405))
# print(35*119)
# print(gcd(17,4165))
# print(gcd(17,lcm(35, 119)))

# arrayA = [14, 35, 119]
# arrayB = [18, 30, 102]

# arrayA =[10, 17]
# arrayB =[5, 20]
# re = 0

# def solution(arrayA, arrayB):
# 	gcda = arrayA[0]
# 	tmparr = arrayA[1:]
# 	while len(tmparr) >= 2:
# 		a = tmparr.pop()
# 		b = tmparr.pop()
# 		tmparr.append(lcm(a,b))
# 	gcdF = gcd(gcda,tmparr[0])
# 	for j in arrayB:
# 		if j % gcdF == 0:
# 			return 0
# 		else:
# 			continue
# 	return gcdF
# print(solution(arrayA, arrayB))

arrayA =[10, 20]
arrayB =[5, 17]
re=10



def gcd(x,y):
	while y > 0:
		x,y = y , x % y
	return x

def lcm(x,y):
	return x*y // gcd(x,y)

def notDiv(array, gcd):
	for n in array:
		if n % gcd == 0:
			return False
	return True

def solution(arrayA, arrayB):
	answer = 0

	gcdA = arrayA[0]
	gcdB = arrayB[0]

	for n in arrayA[1:]:
		gcdA = gcd(n, gcdA)

	for n in arrayB[1:]:
		gcdB = gcd(n, gcdB)

	if notDiv(arrayA, gcdB):
		answer = max(answer, gcdB)

	if notDiv(arrayB, gcdA):
		answer = max(answer, gcdA)

	return answer



# def solution(arrayA, arrayB):
# 	answer = 0
# 	a=arrayA[0]
# 	b=arrayB[0]

# 	for i in range(len(arrayA)):
# 		a=gcd(a,arrayA[i])
# 		b=gcd(b,arrayB[i])
# 		print(a,b)
# 	cheA=1
# 	cheB=1
# 	for i in range(len(arrayA)):
# 		if arrayA[i] % b==0:
# 			cheA=0
# 		if arrayB[i] % a==0:
# 			cheB=0
# 	if cheA==0 and cheB==0:
# 		return cheA
# 	else:
# 		return max(a,b)
