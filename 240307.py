# import sys
# input = sys.stdin.readline

# 회전 초밥
# https://www.acmicpc.net/problem/15961



# from collections import deque,defaultdict

# n,d,k,c = map(int,input().split())
# arr = [int(input()) for _ in range(n)]


# q = deque()
# cnts = defaultdict(int)


# for i in range(k):
# 	q.append(arr[i])
# 	cnts[arr[i]] += 1


# cnt = len(cnts)
# res = 0

# if not cnts[c]:
# 	res = cnt+1


# for start in range(n-1):
# 	prev = q.popleft()
# 	cnts[prev] -= 1

# 	if not cnts[prev]:
# 		cnt-=1

# 	q.append(arr[(start+k)%n])
# 	cnts[q[-1]] += 1

# 	if cnts[q[-1]] == 1:
# 		cnt+=1

# 	if not cnts[c]:
# 		res=max(res,cnt+1)
# 	else:
# 		res = max(cnt,res)
# print(res)

# 수열
# https://www.acmicpc.net/problem/2559


# n,k = map(int,input().split())
# arr = list(map(int,input().split()))
# ans =[]
# ans.append(sum(arr[:k]))


# for i in range(n-k):
# 	ans.append(ans[i]-arr[i]+arr[k+i])
# print(max(ans))

# 게으른 백곰
# https://www.acmicpc.net/problem/10025

# n,k = map(int,input().split())
# arr = []
# m = 0
# for _ in range(n):
# 	x,g = map(int,input().split())
# 	m = max(m,g)
# 	arr.append([x,g])

# visit = [0] * (m+1)
# for x,g in arr:
# 	visit[g] = x
# ans = [0] * (m+1)
# for i in range(1,m+1):
# 	if i - k > 0:
# 		ans[i]+=sum(visit[i-k:i+1])
# 	else:

# 	if i +k <m:
# 		ans[i]+=visit[i+k]


# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())
# numbers = [0] * 1000001
# end = 0
# for i in range(n):
# 	g,x = map(int,input().split())
# 	numbers[x]=g
# 	end = max(x,end)

# step = 2 * k + 1
# window = sum(numbers[:step])
# answer = window
# for i in range(step,end+1):
# 	window += numbers[i] - numbers[i-step]
# 	answer  = max(answer,window)
# print(answer)


# 꿀 아르바이트
# https://www.acmicpc.net/problem/12847


# n,m = map(int,input().split())
# arr = list(map(int,input().split()))

# ans = sum(arr[:m])
# answer = ans

# for i in range(m,n):
# 	ans+= arr[i]- arr[i-m]
# 	answer = max(answer,ans)
# print(answer)


# DNA 비밀번호
# https://www.acmicpc.net/problem/12891

# import sys
# input = sys.stdin.readline
# s,p = map(int,input().split())
# string = input().rstrip()
# a,c,g,t = map(int,input().split())
# d = {'A':0,'C':0,'G':0,'T':0}

# for i in string[:p]:
# 	d[i] +=1


# cnt = 0
# if d['A'] >= a and d['C']>=c and d['G'] >= g and d['T'] >= t:
# 	cnt+=1
# start = 0
# end = start+p

# for i in range(s-p):
# 	d[string[start+i]] -=1
# 	d[string[end+i]] +=1
# 	if d['A'] >= a and d['C']>=c and d['G'] >= g and d['T'] >= t:
# 		cnt+=1
# print(cnt)


# import sys
# input = sys.stdin.readline

# n, k, b = map(int,input().split())
# trafficLight = [i for i in range(1,n+1)]

# for i in range(b):
# 	trafficLight[int(input())-1] = -1

# res = 0
# for i in range(k):
# 	if trafficLight[i] == -1:
# 		res += 1

# count = res
# for i in range(1,n-k+1):
# 	if trafficLight[i-1] == -1:
# 		count -=1
# 	if trafficLight[i+k-1] == -1:
# 		count += 1

# 	res = min(res, count)

# print(res)
