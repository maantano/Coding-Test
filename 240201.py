# 비트마스크
# https://www.acmicpc.net/problem/11723
# import sys
# input = sys.stdin.readline
# n = int(input())

# bit = 0
# for i in range(n):
# 	p = input().split()

# 	if p[0] == 'all':
# 		bit = (1 << 20) - 1
# 	elif p[0] == 'empty':
# 		bit = 0
# 	else:
# 		op = p[0]
# 		num = int(p[1]) - 1

# 		if op == 'add':
# 			bit |= (1 << num)
# 		elif op == 'remove':
# 			bit &= ~(1<<num)
# 		elif op == 'check':
# 			if bit & (1<<num) == 0:
# 				print(0)
# 			else:
# 				print(1)
# 		elif op == 'toggle':
# 			bit = bit ^ (1 << num)


# 도영이가 만든 맛있는 음식
# https://www.acmicpc.net/problem/2961

# 각 재료의 신맛 S와 쓴맛 B를 알고 있다.
# 신맛의 곱이고, 쓴맛은 합이다.
# 도영이는 재료를 적절히 섞어서 요리의 신맛과 쓴맛의 차이를 작게 만들려고 한다. 또, 물을 요리라고 할 수는 없기 때문에, 재료는 적어도 하나 사용해야 한다.
# 재료의 신맛과 쓴맛이 주어졌을 때, 신맛과 쓴맛의 차이가 가장 작은 요리를 만드는 프로그램을 작성하시오.

# n = int(input())

# arr = [list(map(int,input().split())) for _ in range(n)]
# answer = int(1e9)
# if n == 1:
# 	print(abs(arr[0][1]-arr[0][0]))
# else:
# 	for i in range(n):
# 		s,b = arr[i]
# 		for j in range(i+1,n):
# 			s*=arr[j][0]
# 			b+=arr[j][1]
# 			if abs(s-b) < answer:
# 				answer = abs(s-b)
# 	print(answer)

# def dfs(d,cnt,s,b):
# 	global result

# 	if cnt != 0:
# 		if abs(s-b) < result:
# 			result = abs(s-b)

# 	if d == n:
# 		return

# 	dfs(d+1,cnt+1,s*arr[d][0],b+arr[d][1])
# 	dfs(d+1,cnt,s,b)

# n = int(input())
# arr =[list(map(int,input().split())) for _ in range(n)]
# result = int(1e9)
# dfs(0,0,1,0)

# print(result)


# import sys
# input = sys.stdin.readline

# max = int(1e9)

# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]

# answer = int(1e9)

# for i in range(1,1<<n):
# 	s = 1
# 	b = 0
# 	for j in range(n):
# 		if (i & (1<<j)) != 0:
# 			s*=arr[j][0]
# 			b+=arr[j][1]
# 	answer = min(answer,abs(s-b))
# print(answer)

# n = int(input())
# answer = 0

# for i in range(7):
# 	print(1<<i)
# 	if n & (1 << i):
# 		answer+=1
# print(answer)
# n = int(input())
# ans = 0
# for i in range(1, (1<<7)):
# 	if n & (1<<i) :
# 		ans+=1
# print(ans)
# x = int(input())
# count = 0
# n = 64
# while x > 0:
# 	if n > x:
# 		n= n//2
# 	else:
# 		count+=1
# 		x -= n
# print(count)

# n = int(input())
# arr = [list(map(int,input().split(' '))) for _ in range(n)]


# def chk(idx,first,second):
# 	if idx == n:
# 		if len(first) != n/2:
# 			return -1
# 		if len(second) != n/2:
# 			return -1
# 		t1 = 0
# 		t2 = 0
# 		for i in range(n//2):
# 			for j in range(n//2):
# 				if i == j:
# 					continue
# 				t1 += arr[first[i]][first[j]]
# 				t2 += arr[second[i]][second[j]]
# 		diff = abs(t1 - t2)
# 		return diff
# 	ans = -1
# 	t1 = chk(idx+1,first+[idx],second)
# 	if ans == -1 or (t1 != -1 and ans>t1):
# 		ans = t1
# 	t2 = chk(idx+1,first,second+[idx])
# 	if ans == -1 or (t2 != -1 and ans > t2):
# 		ans = t2
# 	return ans

# print(chk(0,[],[]))



# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]

# def dfs(cnt,first,second):
# 	if cnt == n:
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
# 				t1 += arr[first[i]][first[j]]
# 				t2 += arr[second[i]][second[j]]

# 		diff = abs(t1-t2)
# 		return diff
# 	if len(first) > n//2:
# 		return -1
# 	if len(second) > n//2:
# 		return -1
# 	ans = -1

# 	t1 = dfs(cnt+1,first+[cnt],second)
# 	if ans == -1 or (t1 != -1 and t1 < ans):
# 		ans = t1

# 	t2= dfs(cnt+1,first,second+[cnt])
# 	if ans == -1 or (t2 != -1 and t2 < ans):
# 		ans = t2
# 	return ans

# print(dfs(0,[],[]))

# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]

# def go(idx,first,second):
# 	if idx == n:

# 		if len(first) == 0:
# 			return -1
# 		if len(second) == 0:
# 			return -1

# 		t1 = 0
# 		t2 = 0

# 		for i in first:
# 			for j in first:
# 				if i == j:
# 					continue
# 				t1+= arr[i][j]

# 		for i in second:
# 			for j in second:
# 				if i == j:
# 					continue
# 				t2+= arr[i][j]

# 		diff = abs(t1-t2)
# 		return diff

# 	ans = -1
# 	t1 = go(idx+1,first+[idx],second)
# 	if ans == -1 or (t1 != -1 and ans > t1):
# 		ans = t1

# 	t2 = go(idx+1,first,second+[idx])
# 	if ans == -1 or (t2 != -1 and ans > t2):
# 		ans = t2
# 	print('t1 & t2 & ans ===>',t1,t2,ans)
# 	return ans
# print(go(0,[],[]))


# n = int(input())
# s = [list(map(int,input().split())) for _ in range(n)]

# ans = -1

# for i in range((1<<n)):
# 	cnt = 0
# 	for j in range(n):
# 		if (i & (1 << j)) > 0:
# 			cnt +=1
# 		if cnt != n // 2:
# 			continue
# 	first = []
# 	second = []

# 	for j in range(n):
# 		if (i & (1<<j)) > 0:
# 			first += [j]
# 		else:
# 			second += [j]
# 	if len(first) != n//2:
# 		continue

# 	t1 = 0
# 	t2 = 0

# 	for l1 in range(n//2):
# 		for l2 in range(n//2):
# 			if l1 == l2:
# 				continue
# 			t1 += s[first[l1]][first[l2]]
# 			t2 += s[second[l1]][second[l2]]
# 	diff = abs(t1-t2)

# 	if ans == -1 or ans > diff:
# 		ans = diff
# print(ans)

# https://www.acmicpc.net/problem/10971

# def next_permu(arr):

# 	i = len(arr)- 1
# 	while i > 0 and arr[i-1] >= arr[i]:
# 		i-=1

# 	if i <= 0:
# 		return False

# 	j = len(arr) - 1
# 	while arr[i-1] >= arr[j]:
# 		j-=1

# 	arr[i-1],arr[j] = arr[j],arr[i-1]

# 	j = len(arr) - 1

# 	while i < j:
# 		arr[i],arr[j] = arr[j],arr[i]
# 		i+=1
# 		j-=1
# 	return True

# n = int(input())
# w = [list(map(int,input().split())) for _ in range(n)]
# d = list(range(n))

# ans = int(1e9)

# while True:
# 	ok = True
# 	s = 0
# 	for i in range(n-1):
# 		if w[d[i]][d[i+1]] == 0:
# 			ok = False
# 			break
# 		else:
# 			s += w[d[i]][d[i+1]]
# 	if ok and w[d[-1]][d[0]] != 0:
# 		s += w[d[-1]][d[0]]
# 		ans = min(ans,s)

# 	if not next_permu(d):
# 		break
# 	if d[0] != 0:
# 		break
# print(ans)



# def dfs(idx,arr):
# 	if idx == n:
# 		s = 0
# 		for i in range(1,len(arr)):


# 		# return sum(arr)


# 	for i in range(n):
# 		for j in range(i+1,n):
# 			# dfs(idx+1,arr+[[i,j]])


# 부분수열의 합
# https://www.acmicpc.net/problem/1182


# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# count = 0

# def dfs(cnt,s):
# 	global count

# 	if cnt == n:
# 		return

# 	s += arr[cnt]
# 	if m == s:
# 		count+=1

# 	dfs(cnt+1,s-arr[cnt])
# 	dfs(cnt+1,s)
# dfs(0,0)
# print(count)

# for i in range(1,1<<n):
# 	s = sum(arr[k] for k in range(n) if (i & (1<<k)) > 0 )
# 	if m == s:
# 		cnt+=1
# print(cnt)



# n,m = map(int,input().split())
# arr =[list(map(int,input())) for _ in range(n)]

# ans = 0
# for s in range(1<<(n*m)):
# 	sum = 0

# 	for i in range(n):
# 		cur = 0
# 		for j in range(m):
# 			k = i * m + j
# 			if (s & (1<<k)) == 0: #가로 확인 (0)
# 				cur = cur * 10 + arr[i][j]
# 			else:
# 				sum += cur
# 				cur = 0
# 		sum += cur
# 	for j in range(m):
# 		cur = 0
# 		for i in range(n):
# 			k = i * m + j
# 			if (s & (1 << k)) !=0: #세로 확인 (1)
# 				cur = cur * 10 + arr[i][j]
# 			else:
# 				sum += cur
# 				cur = 0
# 		sum += cur
# 	ans = max(ans,sum)
# print(ans)


# 먼저 같은 양의 물이 들어있는 물병 두 개를 고른다.
# 그 다음에 한 개의 물병에 다른 한 쪽에 있는 물을 모두 붓는다.

# 이 방법을 필요한 만큼 계속 한다.

# n,k = map(int,input().split())
# cnt = 0
# while bin(n).count('1') > k:
# 	n+=1
# 	cnt+=1
# print(cnt)


#  메모리 초과 시 & 간초과
# import sys
# sys.setrecursionlimit(10000000)
# n = int(input())
# dp = [0]* (n+1)
# dp[1] = 1


# Top - Down
# def go(chk):
# 	if chk == 1:
# 		return 0
# 	if dp[chk] > 0:
# 		return dp[chk]
# 	dp[chk] = go(chk-1) + 1
# 	if chk % 2 == 0:
# 		tmp = go(chk//2) + 1
# 		dp[chk] = min(tmp,dp[chk])
# 	if chk % 3 == 0:
# 		tmp = go(chk//3) + 1
# 		dp[chk] = min(tmp,dp[chk])
# 	return dp[chk]
# print(go(n))

# Bottom - Up
# n = int(input())
# dp = [0] * (n+1)
# dp[1] = 0
# for i in range(2,n+1):
# 	dp[i] = dp[i-1]+1
# 	if i % 2 == 0 and dp[i] > dp[i//2] + 1:
# 		dp[i] = dp[i//2] + 1
# 	if i % 3 == 0 and dp[i] > dp[i//3] + 1:
# 		dp[i] = dp[i//3]+1
# print(dp[n])

# 종이 조각
# https://www.acmicpc.net/problem/14391
# n,m = map(int,input().split())
# arr = [list(map(int,input())) for _ in range(n)]
# ans = 0


# for s in range(1<<n*m):
# 	sum = 0
# 	for i in range(n):
# 		cur = 0
# 		for j in range(m):
# 			k = i * m + j
# 			if (s & (1 << k) ==0):
# 				cur = cur * 10 + arr[i][j]
# 			else:
# 				sum += cur
# 				cur = 0
# 		sum+=cur
# 	for j in range(m):
# 		cur = 0
# 		for i in range(n):
# 			k = i * m + j
# 			if (s & (1 << k) != 0):
# 				cur = cur * 10 + arr[i][j]
# 			else:
# 				sum += cur
# 				cur = 0
# 		sum+=cur
# 	ans = max(ans,sum)
# print(ans)

# 가르침
# https://www.acmicpc.net/problem/1062
# 김지민은 K개의 글자를 가르칠 시간 밖에 없다.
# 3,6


# import sys
# n,k = map(int,input().split())


# if k < 5:
# 	print(0)
# 	exit()
# elif k == 26:
# 	print(n);
# 	exit();

# answer = 0
# words = [set(input().rstrip()) for _ in range(n)]
# learn = [0] * 26


# for c in ('a','c','i','n','t'):
# 	learn[ord(c)-ord('a')] = 1


# def dfs(idx,cnt):
# 	global answer

# 	if cnt == k - 5:
# 		readcnt = 0
# 		for word in words:
# 			check = True
# 			for w in word:
# 				if not learn[ord(w) - ord('a')]:
# 					check = False
# 					break
# 			if check:
# 				readcnt += 1
# 		answer = max(answer,readcnt)
# 		return
# 	for i in range(idx,26):
# 		if not learn[i]:
# 			learn[i] = True
# 			dfs(i,cnt+1)
# 			learn[i] = False
# dfs(0,0)
# print(answer)

# import sys
# from itertools import combinations

# input = sys.stdin.readline

# def word2bit(word):
# 	bit = 0
# 	for char in word:
# 		bit = bit | (1 << ord(char) - ord('a'))
# 	return bit

# N, K = map(int, input().split())
# words = [input().rstrip() for _ in range(N)]
# bits = list(map(word2bit, words))
# base_bit = word2bit('antic')

# if K < 5:
# 	print(0)
# else:
# 	alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
# 	answer = 0
# 	for combination in combinations(alphabet,K-5):
# 		know_bit = sum(combination) | base_bit
# 		count = 0
# 		for bit in bits:
# 			if bit & know_bit == bit:
# 				count+=1
# 		answer = max(answer,count)
# 	print(answer)


# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())
# arr = [set(input().rstrip()) for _ in range(n)]
# chk = [0] * 26

# for i in 'antic':
# 	idx = ord(i) - ord('a')
# 	chk[idx] = 1

# answer = 0
# def dfs(idx,cnt):
# 	global answer
# 	if cnt == k - 5:
# 		readCnt = 0
# 		for words in arr:
# 			check = True
# 			for word in words:
# 				if not chk[ord(word) - ord('a')]:
# 					check = False
# 					break
# 			if check:
# 				readCnt +=1
# 		answer = max(readCnt,answer)
# 		return
# 	for i in range(idx,26):
# 		if not chk[i]:
# 			chk[i] = 1
# 			dfs(i,cnt+1)
# 			chk[i] = 0

# dfs(0,0)
# print(answer)

# answer = 0
# words = [set(input().rstrip()) for _ in range(n)]
# learn = [0] * 26
# for c in ('a','c','i','n','t'):
# 	learn[ord(c)-ord('a')] = 1

# def dfs(idx,cnt):
# 	global answer

# 	if cnt == k - 5:
# 		readcnt = 0
# 		for word in words:
# 			check = True
# 			for w in word:
# 				if not learn[ord(w) - ord('a')]:
# 					check = False
# 					break
# 			if check:
# 				readcnt += 1
# 		answer = max(answer,readcnt)
# 		return
# 	for i in range(idx,26):
# 		if not learn[i]:
# 			learn[i] = True
# 			dfs(i,cnt+1)
# 			learn[i] = False
# dfs(0,0)
# print(answer)









# 1로 만들기
# https://www.acmicpc.net/problem/1463


# n = int(input())
# d = [0] * (n+1)
# d[1] = 0

# for chk in range(2,n+1):
# 	d[chk] = d[chk-1] + 1
# 	if chk % 2 == 0 and d[chk] > (d[chk//2] + 1):
# 		d[chk] = d[chk//2] + 1
# 	if chk % 3 == 0 and d[chk] > (d[chk//3] + 1):
# 		d[chk] = d[chk//3] + 1
# print(d[n])


# 2×n 타일링
# https://www.acmicpc.net/problem/11726

# n = int(input())
# d = [0] * (n+1)
# d[1] = 1
# d[2] = 2
# for i in range(3,n+1):
# 	d[i] = (d[i-1] + d[i-2]) % 10007

# print(d[n])

# 2×n 타일링 2
# https://www.acmicpc.net/problem/11727

# 1*2, 2*1 , 2*2
# n = int(input())
# d = [0] * (1001)
# d[0] = 1
# d[1] = 1

# for i in range(2,n+1):
# 	d[i] = ((d[i-2] * 2) + d[i-1]) % 10007
# print(d[n])

# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

# t = int(input())
# d = [0] * 11
# d[1] = 1
# d[2] = 2
# d[3] = 4
# for i in range(4,11):
# 	d[i] = d[i-1] + d[i-2] + d[i-3]
# for i in range(t):
# 	chk = int(input())
# 	print(d[chk])

# 카드 구매하기
# https://www.acmicpc.net/problem/11052

# n = int(input())
# arr = [0]+list(map(int,input().split()))
# d = [0] * (n+1)
# for i in range(1,n+1):
# 	for j in range(1,i+1):
# 		d[i] = max(d[i],d[i-j] + arr[j])
# print(d[n])

# 카드 구매하기 2
# https://www.acmicpc.net/problem/16194

# n = int(input())
# d = [int(1e9)] * (n+1)
# d[0] = 0
# arr = [0] + list(map(int,input().split()))
# for i in range(1,n+1):
# 	for j in range(1,i+1):
# 		d[i] = min(d[i],d[i-j]+arr[j])
# print(d[n])

# 1, 2, 3 더하기 5
# https://www.acmicpc.net/problem/15990



# n = int(input())
# d = [[0] * 4 for _ in range(100001)]
# for i in range(1,100001):
# 	if i -1 >= 0:
# 		d[i][1] = d[i-1][2] + d[i-1][3]
# 		if i == 1:
# 			d[i][1] = 1
# 	if i -2 >=0:
# 		d[i][2] = d[i-2][1] + d[i-2][3]
# 		if i == 2:
# 			d[i][2] = 1
# 	if i -3 >=0:
# 		d[i][3] = d[i-3][1] + d[i-3][2]
# 		if i == 3:
# 			d[i][3] = 1
# 	d[i][1] %= 1000000009
# 	d[i][2] %= 1000000009
# 	d[i][3] %= 1000000009

# for i in range(n):
# 	chk = int(input())
# 	print(sum(d[chk]) %1000000009)

# 쉬운 계단 수
# https://www.acmicpc.net/problem/10844


# d = [[0]*10 for _ in range(101)]
# mod = 1000000000
# n = int(input())

# for i in range(1,10):
# 	d[1][i] = 1
# for i in range(2,n+1):
# 	for j in range(10):
# 		d[i][j] = 0
# 		if j - 1 >=0:
# 			d[i][j] += d[i-1][j-1]
# 		if j + 1 <= 9:
# 			d[i][j] += d[i-1][j+1]
# 		d[i][j] %= mod
# ans = sum(d[n]) % mod
# print(ans)


# # 이친수
# # https://www.acmicpc.net/problem/2193

# d = [0]*91
# n = int(input())
# d[1] = 1
# d[2] = 1
# for i in range(3, n+1):
# 	d[i] = d[i-1] + d[i-2]
# print(d[n])


#

# n = int(input())
# d = [0]*(n+1)
# for i in range(1, n+1):
# 	d[i] = i
# 	j = 1
# 	while j*j <= i:
# 		if d[i] > d[i-j*j]+1:
# 			d[i] = d[i-j*j]+1
# 		j += 1
# print(d)
# print(d[n])

# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# d = [[0] * 3 for _ in range(n)]
# for i in range(n):
# 	for j in range(n):
# 		if j == 0:
# 			d[i][0] = min(d[i-1][1],d[i-1][2])  + arr[i][0]
# 		if j == 1:
# 			d[i][1] = min(d[i-1][0],d[i-1][2] )+ arr[i][1]
# 		if j == 2:
# 			d[i][2] = min(d[i-1][0],d[i-1][1]) + arr[i][2]
# print(min(d[n-1]))


# n = int(input())
# d = [[0,0,0] for _ in range(n+1)]
# d[0][0] = 1
# for i in range(1,n+1):
# 	d[i][0] = d[i-1][0] + d[i-1][1] + d[i-1][2]
# 	d[i][1] = d[i-1][0] + d[i-1][2]
# 	d[i][2] = d[i-1][0] + d[i-1][1]
# 	for j in range(3):
# 		d[i][j] %= 9901
# print(sum(d[n])%9901)


# 오르막수
# https://www.acmicpc.net/problem/11057

# d = [[0]*10 for _ in range(1001)]
# mod = 10007
# n =int(input())
# for i in range(10):
# 	d[1][i] = 1

# for i in range(2,n+1):
# 	for j in range(10):
# 		for k in range(j+1):
# 			d[i][j] += d[i-1][k]
# 			d[i][j] %= 100007
# print(sum(d[n]) % 10007)

# d = [[0]*10 for _ in range(1001)]
# mod = 10007
# n =int(input())
# for i in range(10):
# 	d[1][i] = 1

# for i in range(2,n+1):
# 	for j in range(10):
# 		d[i][j] = sum(d[i-1][k] for k in range(10) if k <= j) % 10007

# print(sum(d[n]) % 10007)

# 포도주 시식
# https://www.acmicpc.net/problem/2156

# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.


# n = int(input())
# arr = [0]+[int(input()) for _ in range(n)]

# d = [0] * (n+1)
# d[1] = arr[1]
# if n >= 2:
# 	d[2] = arr[1]+arr[2]

# for i in range(3,n+1):
# 	d[i] = max(d[i-2]+arr[i],d[i-1],d[i-3]+arr[i-1]+arr[i])
# print(d)



# https://www.acmicpc.net/problem/1932

# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]
# d = [[0]*n for i in range(n)]

# d[0][0] = a[0][0]
# for i in range(1, n):
# 	for j in range(0, i+1):
# 		d[i][j] = d[i-1][j] + a[i][j]
# 		if j-1 >= 0 and d[i][j] < d[i-1][j-1] + a[i][j]:
# 			d[i][j] = d[i-1][j-1] + a[i][j]
# print(d)
# print(max(d[n-1]))

# 연속합
# https://www.acmicpc.net/problem/1912
# n = int(input())
# arr = [0]+list(map(int,input().split()))
# d = [-1001]*(n+1)
# d[1] = arr[1]
# for i in range(2,n+1):
# 	d[i] = max(d[i-1]+arr[i],arr[i])
# print(max(d))


# 가장 긴 증가하는 부분 수열 4
# https://www.acmicpc.net/problem/14002

# n = int(input())
# a = list(map(int,input().split()))

# d = [0] * n
# v = [-1] * n
# for i in range(n):
# 	d[i] = 1
# 	for j in range(i):
# 		if a[j] < a[i] and d[j]+1>d[i]:
# 			d[i] = d[j]+1
# 			v[i] = j
# ans = max(d)
# print(ans)
# p = [k for k,v in enumerate(d) if v == ans][0]
# def go(p):
# 	if p == -1:
# 		return
# 	go(v[p])
# 	print(a[p],end=' ')
# go(p)
# print()


# 가장 큰 증가하는 부분 수열
# https://www.acmicpc.net/problem/11055


# n = int(input())
# arr = list(map(int,input().split()))
# d=[0]*n

# for i in range(n):
# 	d[i] = arr[i]
# 	for j in range(i):
# 		if arr[j] < arr[i] and d[j] + arr[i] > d[i]:
# 			d[i] = d[j] + arr[i]
# print(max(d))



# 가장 긴 감소하는 부분 수열
# https://www.acmicpc.net/problem/11722


# n = int(input())
# arr = list(map(int,input().split()))
# d = [0] * n

# for i in range(n-1,-1,-1):
# 	d[i] = 1
# 	for j in range(i+1,n):
# 		if arr[i] > arr[j] and d[i] < d[j]+1:
# 			d[i] = d[j]+1
# 		print(d)
# print(d)

# 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054

# n = int(input())
# arr = list(map(int,input().split()))

# d1 = [0]*n
# d2 = [0]*n

# for i in range(n):
# 	d1[i] = 1
# 	idx = 0
# 	for j in range(i):
# 		if arr[j] < arr[i] and d1[j]+1 > d1[i]:
# 			d1[i] = d1[j]+1

# for i in range(n-1,-1,-1):
# 	d2[i] = 1
# 	for j in range(i+1,n):
# 		if arr[j] < arr[i] and d2[j]+1 > d2[i]:
# 			d2[i] = d2[j]+1
# answer = [d1[i]+d2[i]-1 for i in range(n)]
# print(max(answer))



# 타일 채우기
# https://www.acmicpc.net/problem/2133

#!/usr/bin/python3
# n = int(input())
# d = [0]*(n+1)
# d[0] = 1
# for i in range(2, n+1, 2):
# 	d[i] = d[i-2] * 3
# 	for j in range(i-4, -1, -2):
# 		d[i] += d[j] * 2
# print(d[n])

#!/usr/bin/python3
# n = int(input())
# d = [0]*(n+1)
# d[0] = 1
# for i in range(2, n+1, 2):
# 	d[i] = d[i-2] * 3
# 	for j in range(i-4, -1, -2):
# 		d[i] += d[j] * 2
# print(d[n])

# n=int(input())
# d= [0] * (n+1)
# d[0] = 1
# d[1] = 0
# d[2] = 3

# for i in range(2,n+1,2):
# 	d[i] = d[i-2] * 3
# 	for j in range(i-4,-1,-2):
# 		d[i] += d[j] * 2
# print(d[n])

# n,m = map(int,input().split())
# arr = [[] for _ in range(n)]
# for i in range(m):
# 	a,b = map(int,input().split())
# 	arr[a].append(b)
# 	arr[b].append(a)

# visited = [0] * 2001
# answer = False

# def chk(idx,d):
# 	global answer
# 	visited[idx] = 1
# 	if d == 4:
# 		answer = True
# 		return

# 	for i in arr[idx]:
# 			if not visited[i]:
# 				visited[i] = 1
# 				chk(i,d+1)
# 				visited[i] = 0

# for i in range(n):
# 	chk(i,0)
# 	visited[i] = False
# 	if answer:
# 		break

# if answer:
# 	print(1)
# else:
# 	print(0)

# 빙산
# https://www.acmicpc.net/problem/2573

# from collections import deque
# n,m = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]
# year = 0

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
# 	global year
# 	q = deque([(x,y)])
# 	visited[x][y] = 1
# 	seaList =[]
# 	while q:
# 		x,y = q.popleft()
# 		sea = 0
# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y
# 			if 0<= nx < n and 0<= ny < m:
# 				if not arr[nx][ny]:
# 					sea+=1
# 				if arr[nx][ny] and not visited[nx][ny]:
# 					visited[nx][ny]= 1
# 					q.append((nx,ny))
# 		if sea > 0:
# 			seaList.append((x,y,sea))
# 	for x,y,sea in seaList:
# 		arr[x][y] = max(0,arr[x][y]-sea)
# 	return 1

# ice = []
# for i in range(n):
# 	for j in range(m):
# 		if arr[i][j]:
# 			ice.append((i,j))


# while ice:
# 	visited = [[0] * m for _ in range(n)]
# 	delList = []
# 	group = 0

# 	for i,j in ice:
# 		if arr[i][j] and not visited[i][j]:
# 			group += bfs(i,j)
# 		if not arr[i][j]:
# 			delList.append((i,j))
# 	if group > 1:
# 		print(year)
# 		break
# 	ice = sorted(set(ice) - set(delList))
# 	year+=1

# if group < 2:
# 	print(0)


# 물통
# https://www.acmicpc.net/problem/2251


# from collections import deque
# import sys
# input = sys.stdin.readline

# a,b,c = map(int,input().split())



# q = deque()
# q.append((0,0))

# visited = [[0] * (b+1) for _ in range(a+1)]
# visited[0][0] = 1

# answer = []

# def pour(x,y):
# 	if not visited[x][y]:
# 		visited[x][y] = 1
# 		q.append((x,y))

# def bfs():
# 	while q:

# 		x,y = q.popleft()

# 		z = c - x - y

# 		if x == 0:
# 			answer.append(z)

# 		water = min(x, b - y)
# 		pour(x - water, y + water)
# 		# A에서 C로 물 이동
# 		water = min(x, c - z)
# 		pour(x - water, y)

# 		# B에서 C로 물 이동
# 		water = min(y, c - z)
# 		pour(x, y - water)
# 		# B에서 A로 물 이동
# 		water = min(y, a - x)
# 		pour(x + water, y - water)

# 		# C에서 A로 물 이동
# 		water = min(z, a - x)
# 		pour(x + water, y)
# 		# C에서 B로 물 이동
# 		water = min(z, b - y)
# 		pour(x, y + water)




# pyp3
# https://www.acmicpc.net/problem/2458
# n,m = map(int,input().split())
# arr = [[0]*(n+1) for _ in range(n+1)]
# for i in range(n):
# 	a,b = map(int,input().split())
# 	arr[a][b] = 1

# for k in range(1,n+1):
# 	for i in range(1,n+1):
# 		for j in range(1,n+1):
# 			if not arr[i][j]:
# 				if arr[i][k] and arr[k][j]:
# 					arr[i][j] = 1

# result = 0

# for i in range(1,n+1):
# 	sum = 0
# 	for j in range(1,n+1):
# 		sum += arr[i][j] + arr[j][i]
# 	if sum == n-1:
# 		result +=1
# print(result)


import sys
from collections import deque
input = sys.stdin.readline



import heapq
def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0
	while q:
		dist,now= heapq.heappop(q)
		for node,leaf in arr[now]:
			cost = dist+leaf
			if cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(cost,node))




INF = int(1e9)
t = int(input())
for _ in range(t):
	n,d,c = map(int,input().split())
	arr = [[] for _ in range(n+1)]
	distance = [INF] * (n+1)
	for i in range(d):
		a,b,s = map(int,input().split())
		arr[b].append((a,s))
	dijkstra(c)

	cnt = 0
	ans = 0
	for i in distance:
		if i != INF:
			cnt +=1
			ans = max(ans,i)
	print(f'{cnt} {ans}')




def dji(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0

	while q:
		dist,now = heapq.heappop(q)
		for node,leaf in arr[now]:
			cost = leaf+dist
			if cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(node,cost))


for _ in range(t):
	n,d,c = map(int,input().split())
	arr = [[] for _ in range(n+1)]
	distance = [int(1e9)] *(n+1)

	for i in range(d):
		a,b,s = map(int,input().split())
		arr[b].append((a,s))
	dji(c)

	cnt = 0
	ans = 0
	for i in  distance:
		if i != int(1e9):
			cnt+=1
			ans = max(ans,i)
	print(f'{cnt} {ans}')

