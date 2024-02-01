# import sys
# input = sys.stdin.readline

# n = int(input())

# for i in range(n):
# 	s,t = input().split()
# 	idx = s.find('x')
# 	if idx >= 0:
# 		print(t[idx].upper(),end='')
# 		continue
# 	idx = s.find('X')
# 	if idx >= 0:
# 		print(t[idx].upper(),end='')


# for S, T in map(lambda x: x.split(), [*open(0)][1:]):
# 	i = S.find('X')
# 	if i >= 0: print(T[i].upper(), end=''); continue

# 	i = S.find('x')
# 	if i >= 0: print(T[i].upper(), end=''); continue



# 연탄을 모든 집에 배달하려고 했던 산타는 큰 고민에 빠집니다.
# 각 집에는 연탄 난로가 있는데, 난로와 연탄 모두 원 모양으로 되어있기 때문에 난로의 반지름의 길이가 연탄의 반지름의 길이의 배수인 집에서만 이 연탄을 사용할 수 있다는 것입니다.

# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = sorted(list(map(int,input().split())))
# cnt = 0
# for i in range(n):
# 	tmp = 1
# 	for j in range(n):
# 		if i == j: continue
# 		if arr[j] % arr[i] == 0:
# 			tmp+=1
# 	cnt = max(cnt,tmp)
# print(cnt)



# 차이를 최대로
# https://www.acmicpc.net/problem/10819

# def next_permu(arr):
# 	i = len(arr)-1
# 	while i > 0 and arr[i-1] >= arr[i]:
# 		i-=1

# 	if i <= 0:
# 		return False

# 	j = len(arr) - 1
# 	while arr[j] <= arr[i-1]:
# 		j -= 1
# 	arr[i-1],arr[j] = arr[j],arr[i-1]

# 	j = len(arr) - 1
# 	while i < j:
# 		arr[i],arr[j] = arr[j],arr[i]
# 		j-=1
# 		i+=1

# 	return True


# def cal(arr):
# 	ans = 0
# 	for i in range(1,len(arr)):
# 		ans += abs(arr[i-1]-arr[i])
# 	return ans


# n = int(input())
# arr = sorted(list(map(int,input().split())))

# ans = 0
# while True:
# 	tmp = cal(arr)
# 	ans = max(ans,tmp)
# 	if not next_permu(arr):
# 		break
# print(ans)

# TSP 10971
# def next_permu(arr):
# 	i = len(arr) - 1
# 	while i >0 and arr[i-1]>= arr[i]:
# 		i -= 1
# 	if i <= 0:
# 		return False
# 	j = len(arr) - 1
# 	while arr[i-1] >= arr[j]:
# 		j-=1

# 	arr[i-1],arr[j] = arr[j], arr[i-1]

# 	j = len(arr) - 1
# 	while i < j:
# 		arr[i],arr[j] = arr[j],arr[i]
# 		i += 1
# 		j-=1
# 	return True


# n = int(input())
# w = [list(map(int,input().split())) for _ in range(n)]
# d = list(range(n))
# ans = int(1e9)

# while True:
# 	ok = True
# 	s = 0

# 	for i in range(0,n-1):
# 		if w[d[i]][d[i+1]] == 0:
# 			ok = False
# 			break
# 		else:
# 			s += w[d[i]][d[i+1]]
# 	if ok and w[d[-1]][d[0]] != 0:
# 		s+= w[d[-1]][d[0]]
# 		ans = min(ans,s)
# 		print(ans)

# 	print(d)
# 	if not next_permu(d):
# 		break

# print(ans)

n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(1, (1<<n)):
	# s = 0
	# for k in range(n):
	# 	print('k ===>',k)
	# 	if (i & (1<<k) > 0 ):
	# 		s += a[k]
	# print('s ====>',s)
	s = sum(a[k] for k in range(n) if (i & (1<<k)) > 0)
	if m == s:
		ans += 1
print(ans)

