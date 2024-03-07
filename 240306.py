import sys
input = sys.stdin.readline

# 회전 초밥
# https://www.acmicpc.net/problem/2531

# 틀림
# import sys
# input = sys.stdin.readline

# n,d,k,c = map(int,input().split())

# arr = [int(input()) for _ in range(n)]
# ans = 0
# for i in range(n):
# 	tmp = []
# 	cnt = 0
# 	for j in range(i,i+4):
# 		if j >= n:
# 			j-=n
# 		tmp.append(arr[j])
# 	cnt = len(tmp)
# 	if c not in tmp:
# 		cnt +=1
# 	ans = max(ans,cnt)
# print(ans)


# 시간 초과
# n,d,k,c = map(int, input().split())
# plate = []
# for i in range(n):
# 	plate.append(int(input()))

# max_sushi = 0

# #방법1 (시간초과 실패)
# for i in range(n):
# 	tmp = set()
# 	tmp.add(c)
# 	for j in range(k):
# 		tmp.add(plate[i-n+j])
# 	#print(tmp , end=' ')
# 	max_sushi = max(max_sushi, len(tmp))


#슬라이스

# n,d,k,c = map(int, input().split())
# plate = []
# for i in range(n):
# 	plate.append(int(input()))

# max_sushi = 0

# for i in range(n):
# 	if i <= n-k:
# 		tmp = set(plate[i:i+k])
# 	else:
# 		tmp = set(plate[i:])
# 		tmp.update(plate[:(i+k)%n])
# 	tmp.add(c)
# 	max_sushi = max(max_sushi,len(tmp))
# print(max_sushi)

# import sys
# input = sys.stdin.readline

# N, d, k, c = map(int, input().rstrip().split())
# sushi = [int(input()) for _ in range(N)]
# max_number_of_type = 0
# for i in range(N):
# 	if i+k > N:
# 		number_of_type = len(set(sushi[i:N] + sushi[:(i+k)%N] + [c]))
# 	else:
# 		number_of_type = len(set(sushi[i:i+k] + [c]))
# 	if max_number_of_type < number_of_type:
# 		max_number_of_type = number_of_type
# print(max_number_of_type)

# import sys
# input = sys.stdin.readline

# n,d,k,c = map(int,input().split())
# maps = [int(input()) for _ in range(n)]

# left = 0
# right = left+k
# ans = 0

# while right <= n:
# 	tmp = set(maps[left:right])
# 	if c in tmp:
# 		ans = max(ans,len(tmp))
# 	else:
# 		ans = max(ans,len(tmp)+1)

# 	left += 1
# 	right += 1

# right = 1

# while left < n:
# 	tmp = set(maps[left:n] + maps[0:right])
# 	if c in tmp:
# 		ans = max(ans,len(tmp))
# 	else:
# 		ans = max(ans,len(tmp)+1)
# 	left += 1
# 	right+= 1

# print(ans)


# 회전 초밥
# https://www.acmicpc.net/problem/15961

# from collections import deque,defaultdict
# n,d,k,c = map(int,input().split())
# sushi = [int(input()) for _ in range(n)]

# window = deque()
# cnts = defaultdict(int)

# for i in range(k):
# 	cnts[sushi[i]] +=1
# 	window.append(sushi[i])
# res = 0
# cnt = len(cnts)
# if not cnts[c]:
# 	res = cnt+1

# for start in range(n-1):
# 	prev = window.popleft()
# 	cnts[prev] -=1
# 	if not cnts[prev]:
# 		cnt-=1
# 	window.append(sushi[(start+k)%n])
# 	cnts[window[-1]] +=1

# 	if cnts[window[-1]] == 1:
# 		cnt+=1


# 	if cnts[c] == 0:
# 		res=max(res,cnt+1)
# 	else:
# 		res = max(res,cnt)
# print(res)


# from collections import deque,defaultdict
# import sys

# n,d,k,c = map(int,input().split())
# arr = [int(input()) for _ in range(n)]

# window = deque()
# cnts = defaultdict(int)

# for i in range(k):
# 	window.append(arr[i])
# 	cnts[arr[i]] += 1

# cnt = len(cnts)
# res = 0
# if not cnts[c]:
# 	res = cnt+1


# for start in range(n-1):
# 	prev = window.popleft()
# 	cnts[prev] -=1

# 	if not cnts[prev]:
# 		cnt-=1

# 	window.append(arr[(start+k)%n])
# 	cnts[window[-1]]+=1

# 	if cnts[window[-1]] == 1:
# 		cnt+=1

# 	if cnts[c] == 0:
# 		res = max(res,cnt+1)
# 	else:
# 		res = max(res,cnt)
# print(res)


# 트리 만들기
# https://www.acmicpc.net/problem/14244


# n,m = map(int,input().split())
# leaf = 0
# if m == 2:
# 	leaf = 1

# last_leaf = 0

# for i in range(1,n):
# 	if m > leaf:
# 		print(0,i)
# 		leaf+=1
# 	else:
# 		print(last_leaf,i)
# 	last_leaf = i



