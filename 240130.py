# 순서 : n!
# 선택 : 2 ^ n


# https://www.acmicpc.net/problem/15649

# 순서와 관련된 문제.
# N개중에 M개를 고르는 문제
# 123 != 132

# 1,2,...M
# 재귀 : 각각의 자리에 올 수 있는 수를 결정
# 위치만 변했지 올수있는 수를 고르는것

# 1번째 : 1 ~ n 개중에 하나를 고르는데 4를 골랐다면
# 2번째 : 1 ~ n 개중에 하나를 고르는데 4를 빼고 골라야하고 3을 골랐다
# 3번째 : 1 ~ n 개중에 하나를 고르는데 4,3를 빼고 골라야하고 2을 골랐다
# .
# .
# .
# n번쨰 : 남은 1개

# 변하는 것을 캐치해야하는데,
# 1번째, 2번째.. 위치가 변한다!
# 함수의 인자로 들어가야한다.
# 사용한 수가 인자로 들어가야한다.

# n,m = map(int,input().split())
# visited = [0] * (n+1)
# def sol(cnt,arr):
# 	if cnt == m:
# 		print(*arr)
# 		return
# 	for i in range(1,n+1):
# 		if not visited[i]:
# 			visited[i] = 1
# 			sol(cnt+1,arr+[i])
# 			visited[i] = 0
# sol(0,[])

# n,m = map(int,input().split())
# visited = [0] * (n+1)

# def sol(cnt,arr,last):
# 	if cnt == m:
# 		print(*arr)
# 		return
# 	for i in range(last,n+1):
# 		if not visited[i]:
# 			visited[i] = 1
# 			sol(cnt+1,arr+[i],i+1)
# 			visited[i] = 0
# sol(0,[],1)



# https://www.acmicpc.net/problem/15651

# n,m = map(int,input().split())
# def sol(cnt,arr):
# 	if cnt == m:
# 		print(*arr)
# 		return
# 	for i in range(1,n+1):
# 		sol(cnt+1,arr+[i])
# sol(0,[])


# https://www.acmicpc.net/problem/15652
# n,m = map(int,input().split())
# def sol(cnt,arr,last):
# 	if cnt == m:
# 		print(*arr)
# 		return
# 	for i in range(last,n+1):
# 		sol(cnt+1,arr+[i],i)

# sol(0,[],1)


# n = int(input())
# def plus(chk,sum):
# 	global answer
# 	if sum == chk:
# 		answer+=1
# 		return
# 	for i in range(1,4):
# 		if sum+i > chk:
# 			continue
# 		plus(chk,sum+i)

# for i in range(n):
# 	answer = 0
# 	chk = int(input())
# 	plus(chk,0)
# 	print(answer)


# n,m = map(int,input().split())

# vowel = ['a','e','i','o','u']
# alpha = sorted(list(map(str,input().split())))
# visited = [0] * (m+1)

# def chk(arr):
# 	voCnt = 0
# 	alCnt = 0
# 	for i in arr:
# 		if i in vowel:
# 			voCnt+=1
# 		else:
# 			alCnt+=1

# 	if voCnt >= 1 and alCnt >= 2:
# 		return True
# 	else:
# 		return False

# def sol(arr,cnt,idx):
# 	if cnt == n:
# 		if chk(arr):
# 			print(''.join(arr))
# 			return

# 	for i in range(idx,m):
# 		if not visited[i]:
# 			visited[i] = 1
# 			sol(arr+[alpha[i]],cnt+1,i+1)
# 			visited[i] = 0

# sol([],0,0)

# 퇴사
# https://www.acmicpc.net/problem/14501


# n = int(input())
# dateArr = [0] * (n+1)
# valueArr = [0] * (n+1)
# for i in range(1,n+1):
# 	dateArr[i],valueArr[i] = map(int,input().split())
# ans = 0
# min = int(1e9)

# def go(day,s):
# 	global ans

# 	if day == n+1:
# 		ans = max(ans,s)
# 		return
# 	if day > n+1:
# 		return
# 	go(day+1,s)
# 	go(day+dateArr[day],s+valueArr[day])

# go(1,0)
# print(ans)

# def go(index, first, second):
# 	if index == n:
# 		if len(first) != n//2:
# 			return -1
# 		if len(second) != n//2:
# 			return -1

# 		t1 = 0
# 		t2 = 0
# 		for i in range(n//2):
# 			for j in range(n//2):
# 				if i == j:
# 					continue
# 				t1 += s[first[i]][first[j]]
# 				t2 += s[second[i]][second[j]]
# 		diff = abs(t1-t2)
# 		return diff

# 	if len(first) > n//2:
# 		return -1
# 	if len(second) > n//2:
# 		return -1

# 	ans = -1

# 	t1 = go(index+1,first+[index],second)
# 	if ans == -1 or (t1 != -1 and ans > t1 ):
# 		ans = t1

# 	t2 = go(index+1,first,second + [index])
# 	if ans == -1 or (t2 != -1 and ans > t2 ):
# 		ans = t2
# 	return ans


# n = int(input())
# s = [list(map(int,input().split())) for _ in range(n)]
# print(go(0, [], []))

# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]


# def go(index,first,second):
# 	if index == n:
# 		if len(first) > n //2 or len(second) > n // 2:
# 			return -1

# 		t1 = 0
# 		t2 = 0

# 		for i in range(n//2):
# 			for j in range(n//2):
# 				if i == j:
# 					continue
# 				t1 += arr[first[i]][first[j]]
# 				t2 += arr[second[i]][second[j]]

# 		diff = abs(t1-t2)
# 		return diff

# 	if len(first) > n //2 or len(second) > n //2:
# 		return -1


# 	ans = -1
# 	t1 = go(index+1,first+[index],second)
# 	if ans == -1 or (t1 != -1 and ans > t1):
# 		ans =t1

# 	t2 = go(index+1,first,second+[index])
# 	if ans == -1 or (t2 != -1 and ans > t2):
# 		ans = t2
# 	return ans

# print(go(0,[],[]))

# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]


# def go(index,first,second):
# 	if n == index:
# 		if len(first) == 0  or len(second) == 0:
# 			return -1

# 		t1 = 0
# 		t2 = 0

# 		for i in first:
# 			for j in first:
# 				if i == j:
# 					continue
# 				t1+=arr[i][j]

# 		for i in second:
# 			for j in second:
# 				if i == j:
# 					continue
# 				t2+=arr[i][j]

# 		diff = abs(t1-t2)
# 		return diff

# 	ans = -1
# 	t1 = go(index+1,first+[index],second)
# 	if ans == -1 or (t1 != -1 and ans > t1):
# 		ans = t1

# 	t2 = go(index+1,first,second+[index])
# 	if ans == -1 or (t2 != -1 and ans > t2):
# 		ans = t2

# 	return ans


# print(go(0,[],[]))


# 2
# < >

# 9
# > < < < > > > < <

# n = int(input())
# s = list(map(str,input().split()))


# def go(idx,arr):
# 	if idx == n:
# 		print(''.join(arr))
# 		return
# 	for p in s:
# 		for i in range(1,10):
# 			if p == '>':
# 				if arr[i-1] > i:
# 					go(idx+1,arr+[i])
# 			if p == '<':
# 				if arr[i-1] < i:
# 					go(idx+1,arr+[i])
# go(0,[])



# n = int(input())
# s = list(map(str,input().split()))
# chk = [0] * 10
# def good(x,y,op):
# 	if op == '<':
# 		if x > y:
# 			return False
# 	if op == '>':
# 		if x < y:
# 			return False
# 	return True


# ans = []
# def go(idx,num):
# 	if idx == n+1:
# 		ans.append(num)
# 		return

# 	for i in range(10):
# 		if chk[i]:
# 			continue
# 		if idx == 0 or good(num[idx-1],str(i),s[idx-1]):
# 			chk[i] = True
# 			go(idx+1,num+str(i))
# 			chk[i] = False
# go(0,'')
# ans.sort()
# print(ans[-1])
# print(ans[0])



# def chk(idx):
# 	s = 0
# 	for i in range(idx,-1,-1):
# 		s+=ans[i]
# 		if sign[i][idx] == 0:
# 			if s != 0:
# 				return False
# 		elif sign[i][idx] <0:
# 			if s>=0:
# 				return False
# 		elif sign[i][idx]  > 0:
# 			if s <= 0:
# 				return False
# 	return True

# def go(idx):
# 	if idx == n:
# 		return True
# 	if sign[idx][idx] == 0:
# 		ans[idx] = 0
# 		return chk(idx) and go(idx+1)

# 	for i in range(11):
# 		ans[idx] = i * sign[idx][idx]
# 		if chk(idx) and go(idx+1):
# 			return True
# 	return False



# guess
# n = int(input())
# s = input()

# sign = [[0]*n for _ in range(n)]
# ans = [0] * n
# cnt = 0
# for i in range(n):
# 	for j in range(i,n):
# 		if s[cnt] == '0':
# 			sign[i][j] = 0
# 		elif s[cnt] == '+':
# 			sign[i][j] = 1
# 		else:
# 			sign[i][j] = -1
# 		cnt+=1
# go(0)
# print(' '.join(map(str,ans)))

# def check(index):
# 	s = 0
# 	for i in range(index,-1,-1):
# 		s += ans[i]
# 		if sign[i][index] == 0:
# 			if s != 0:
# 				return False
# 		elif sign[i][index] < 0:
# 			if s >= 0:
# 				return False
# 		elif sign[i][index] > 0:
# 			if s <= 0:
# 				return False
# 	return True



# def go(index):
# 	if index == n:
# 		return True
# 	if sign[index][index] == 0:
# 		ans[index] = 0
# 		return check(index) and go(index+1)

# 	for i in range(1, 11):
# 		ans[index] = i * sign[index][index]
# 		if check(index) and go(index+1):
# 			return True
# 	return False

# n = int(input())
# s = input()
# sign = [[0]*n for _ in range(n)]
# ans = [0]*n
# cnt = 0
# for i in range(n):
# 	for j in range(i,n):
# 		if s[cnt] == '0':
# 			sign[i][j] = 0
# 		elif s[cnt] == '+':
# 			sign[i][j] = 1
# 		else:
# 			sign[i][j] = -1
# 		cnt += 1

# go(0)
# print(' '.join(map(str,ans)))

# 1234
# 다음 순열
# https://www.acmicpc.net/problem/10972


# n = int(input())
# arr = list(map(int,input().split()))
# ans = 0
# chk = 0
# chk2 = 0

# def next_permu(arr):
# 	i = len(arr)-1

# 	while i > 0 and arr[i-1] >= arr[i]:
# 		i  -= 1
# 	print('i ===>',i)
# 	if i<= 0:
# 		return False
# 	j = len(arr)-1
# 	while arr[j] <= arr[i-1]:
# 		j -= 1
# 	print('j ===>',j)
# 	arr[i-1],arr[j] = arr[j],arr[i-1]

# 	j = len(arr)-1

# 	while i<j:
# 		arr[i],arr[j] = arr[j],arr[i]
# 		i+=1
# 		j-=1
# 	return True

# n = int(input())
# arr = list(map(int,input().split()))

# if next_permu(arr):
# 	print(' '.join(map(str,arr)))
# else:
# 	print(-1)

# https://www.acmicpc.net/problem/10973
# n = int(input())
# arr = list(map(int,input().split()))


# def prev_permu(arr):
# 	i = len(arr)-1

# 	while i >0 and arr[i-1] <= arr[i]:
# 		i-=1
# 	if i <= 0:
# 		return False

# 	j = len(arr) -1
# 	while arr[j] >= arr[i-1]:
# 		j -=1

# 	arr[i-1],arr[j] = arr[j],arr[i-1]

# 	j = len(arr)-1

# 	while i < j:
# 		arr[i],arr[j] = arr[j],arr[i]
# 		i+=1
# 		j-=1
# 	return True


# if prev_permu(arr):
# 	print(' '.join(map(str,arr)))
# else:
# 	print(-1)




n = int(input())
arr = list(range(1,n+1))
def all_permu(n):
	i = len(arr)-1

	while i > 0 and arr[i-1] >= arr[i]:
		i -=1

	if i <= 0:
		return False

	j = len(arr) -1
	while arr[j] <= arr[i-1]:
		j-=1

	arr[i-1],arr[j] = arr[j],arr[i-1]

	j = len(arr) - 1

	while i< j:
		arr[i],arr[j] = arr[j],arr[i]
		i+=1
		j-=1
	return True

while True:
	print(' '.join(map(str,arr)))
	if not all_permu(arr):
		break







