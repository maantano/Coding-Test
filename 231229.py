# # 2309 일곱 난장이
# n = 9
# arr = sorted([int(input()) for _ in range(n)])
# total = sum(arr)
# remove = []
# for i in range(n):
# 	for j in range(i+1,n):
# 		if total - arr[i] - arr[j] == 100:
# 			for k in arr:
# 				if k == arr[i] or k == arr[j]:
# 					continue
# 				print(k)
# 			exit()


# 1476 날짜 계산
# e,s,m = map(int,input().split())
# eChk=sChk=mChk=1
# year = 1
# while True:
# 	if eChk == e and sChk ==s and  mChk ==m:
# 		print(year)
# 		break

# 	eChk += 1
# 	sChk += 1
# 	mChk += 1
# 	if eChk == 16:
# 		eChk = 1
# 	if sChk == 29:
# 		sChk = 1
# 	if m == 20:
# 		mChk = 1
# 	year += 1

# 3085 사탕 게임
# n = int(input())
# arr = [list(input()) for _ in range(n)]

# chk 반복문을 x축 비교 y축 비교를 나눠서 생각해야한다.
# 한번에 계산하려 하면, 반복문을 도는 와중에 x,y축 비교를 해버려서 계산이 틀어진다.
# def chk(arr):
# 	n = len(arr)
# 	l = 1
# 	for i in range(n):
# 		cnt = 1
# 		for j in range(1,n):
# 			if arr[i][j] == arr[i][j-1]:
# 				cnt+=1
# 			else:
# 				cnt=1
# 			if l < cnt:
# 				l = cnt
# 		cnt = 1
# 		for j in range(1,n):
# 			if arr[j][i] == arr[j-1][i]:
# 				cnt+=1
# 			else:
# 				cnt = 1
# 			if l < cnt:
# 				l = cnt
# 	return l
# # ========================================================================
# def chk(arr):
# 	n = len(arr)
# 	l = 1
# 	for i in range(n):
# 		tmpX = 1
# 		tmpY = 1
# 		for j in range(1,n):
# 			if arr[i][j] == arr[i-1][j]:
# 				tmpX+=1
# 			else:
# 				tmpX=1
# 			if l < tmpX:
# 				l = tmpX
# 			if arr[j][i] == arr[j-1][i]:
# 				tmpY+=1
# 			else:
# 				tmpY = 1
# 			if l < tmpY:
# 				l = tmpY
# 	return l



# answer = 0
# for i in range(n):
# 	for j in range(n):
# 		if j+1 < n:
# 			arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
# 			answer = max(answer,chk(arr))
# 			arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
# 		if i+1 < n:
# 			arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
# 			answer = max(answer,chk(arr))
# 			arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
# print(answer)


# 사탕 게임 연산 줄이기!
def chk(a,startX,endX,startY,endY):
	n = len(a)
	ans = 1
	for i in range(startX,endX+1):
		cnt = 1
		for j in range(1,n):
			if a[i][j] == a[i][j-1]:
				cnt+=1
			else:
				cnt=1
			if ans < cnt:
				ans = cnt
	for i in range(startY,endY+1):
		cnt = 1
		for j in range(1,n):
			if a[j][i] == a[j-1][i]:
				cnt +=1
			else:
				cnt = 1
			if ans < cnt:
				ans = cnt
	return ans

n = int(input())
a = [list(input()) for _ in range(n)]

ans = 0
for i in range(n):
	for j in range(n):
		if j+1 < n:
			a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
			tmp = chk(a,i,i,j,j+1)
			if ans < tmp:
				ans = tmp
			a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
		if i+1 < n:
			a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
			tmp = chk(a,i,i+1,j,j)
			if ans < tmp:
				ans = tmp
			a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
print(ans)




# 1107 리모컨

# 1. 숫자를 다 누른 후 +,- 버튼을 눌러야한다.
# 	1.1) 숫자를 누르다 +,-를 누르고 + 를 누르면 기존 숫자는 다 사라지기 때문에
# 2. +,-는 중 하나의 버튼만 클릭한다.
# 	2.1) +를 누르다 -를 누르거나 하는 경우는 없다.
# 3. 누르지 않는 경우가 있다.
# 	3.1) 출발 번호와 목표번호가 같은 경우
# 4. 이동하려는 채널의 수를 100만 까지 늘려서 생각한다.
# 	4.1) 500,000에 이동해야 하고, 1과 5만 누를 수 있는 경우
#	4.2)155,555 -> 500,000 보다 (+ 344,445번)
#	4.3) 511,111 -> 500,000이 더 좋다. (- 11,111번)

# 1. 이동할 채널 C를 정한다
# 2. C에 포함되어있는 숫자 중에 고장난 버튼이 있는지 확인한다
# 3. 고장난 버튼이 포함되어 있지 않다면 |C- N|을 계산해 +나 - 버튼을 몇 번 눌러야 하는지를 계산한다.

# n = int(input())
# m = int(input())
# broken = [0] * 10
# if m > 0:
# 	btn = list(map(int,input().split()))
# else:
# 	btn = []

# for b in btn:
# 	broken[b] = 1

# def check(chk):
# 	if chk == 0:
# 		if broken[0]:
# 			return 0
# 		else:
# 			return 1
# 	time = 0
# 	while chk > 0:
# 		tmp = chk % 10
# 		if broken[tmp]:
# 			return 0
# 		time+=1
# 		chk //= 10
# 	return time



# ans = abs(n-100)
# for i in range(0,1000001):
# 	c = i
# 	l = check(c)
# 	if l > 0:
# 		press = abs(c-n)
# 		if ans > l + press:
# 			ans = l +press
# print(ans)





# 4948 베르트랑 공준

# 1
# 10
# 13
# 100
# 1000
# 10000
# 100000
# 0

from collections import Counter
MAX = 123456
p =[0] * (MAX+1)
p[0] = p[1] = 1
for i in range(2,MAX+1):
	if not p[i]:
		j = i*2
		while j<=MAX:
			p[j] = 1
			j+=i

while True:
	n = int(input())
	if n == 0:
		break
	else:
		c = Counter(p[n:(2*n)+1])
		print(c[1])


# def prime(x):
# 	for i in range(2,int(x**0.5)+1):
# 		if x % i == 0:
# 			return False
# 		return True
# for i in range(2,MAX+1):
# 	p[i] = prime(i)

# while True:
# 	n = int(input())
# 	if n == 0:
# 		break
# 	else:
# 		print(p[n])
