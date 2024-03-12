
# 정수 제곱근
# https://www.acmicpc.net/problem/2417

# import sys
# input = sys.stdin.readline

# n = int(input())

# start = 0
# end = n

# while start <= end:
# 	mid = (start+end) // 2

# 	if mid ** 2 < n:
# 		start = mid +1
# 	else:
# 		end = mid - 1
# print(mid)


# 어두운 굴다리
# https://www.acmicpc.net/problem/17266

# n = int(input())
# m = int(input())
# arr = list(map(int,input().split()))


# if len(arr) == 1:
# 	h = max(arr[0],n-arr[0])

# else:
# 	h = arr[0]
# 	for i in range(len(arr)):
# 		if i == (len(arr)-1):
# 			tmp = n -arr[-1]
# 		else:
# 			a = arr[i+1] - arr[i]

# 			if a % 2:
# 				tmp = a//2 + 1
# 			else:
# 				tmp = a//2
# 		h = max(h,tmp)
# print(h)

# CD
# https://www.acmicpc.net/problem/4158

# import sys
# input = sys.stdin.readline
# while True:
# 	n,m = map(int,input().split())
# 	if n == 0 and m == 0:
# 		break
# 	cnt = 0
# 	d = {}
# 	for i in range(n):
# 		d[int(input())] = 1

# 	for j in range(m):
# 		tmp = int(input())
# 		if tmp in d:
# 			cnt+=1
# 	print(cnt)


# 선물
# https://www.acmicpc.net/problem/1166
# import sys
# input = sys.stdin.readline
# N, L, W, H = map(int, input().split())
# s, e = 0, max(L, W, H)
# while e-s > 0.00000001:
# 	m = (s+e)/2
# 	if (L//m)*(W//m)*(H//m) >= N:
# 		s = m
# 	else:
# 		e = m
# print("%.10f" %(e))


# 히오스 프로게이머
# https://www.acmicpc.net/problem/16564

# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())

# arr = [int(input()) for _ in range(n)]

# s = min(arr)
# e = s + k
# res = 0

# while s <= e:
# 	m = (s+e) // 2

# 	tmp = 0
# 	for l in arr:
# 		if m > l:
# 			tmp += (m-l)

# 	if tmp <= k:
# 		s = m + 1
# 		res = max(res,m)
# 	else:
# 		e = m - 1
# print(res)




# sort 마스터 배지훈의 후계자
# https://www.acmicpc.net/problem/20551

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())

# arr = sorted([int(input()) for _ in range(n)])
# dic = {}
# for i in range(n):
# 	if arr[i] not in dic:
# 		dic[arr[i]] = i

# d = [int(input()) for _ in range(m)]
# for t in d:
# 	if t in dic:
# 		print(dic[t])
# 	else:
# 		print(-1)

# 선분 위의 점
# https://www.acmicpc.net/problem/11663

# n,m = map(int,input().split())
# arr = sorted(list(map(int,input().split())))

# def minA(x):
# 	s = 0
# 	e = n-1

# 	while s <= e:
# 		m = (s+e) // 2

# 		if x > arr[m]:
# 			s = m + 1
# 		else:
# 			e = m -1
# 	return e + 1

# def maxA(x):
# 	s = 0
# 	e = n-1
# 	while s<=e:
# 		m = (s+e) // 2

# 		if x >= arr[m]:
# 			s = m + 1
# 		else:
# 			e = m - 1
# 	return e


# for i in range(m):
# 	a,b = map(int,input().split())
# 	print(maxA(b)-minA(a) + 1)





# 서버실
# https://www.acmicpc.net/problem/17245

# from sys import stdin

# input = stdin.readline

# def main():
# 	N = int(input())
# 	computers = []
# 	for _ in range(N):
# 		computers += list(map(int, input().split()))

# 	total = sum(computers)
# 	ans = 0
# 	start = 0
# 	end = max(computers)
# 	while start <= end:
# 		mid = (start + end) // 2
# 		sums = 0
# 		for computer in computers:
# 			sums += computer if computer < mid else mid

# 		if sums < total / 2:
# 			start = mid + 1
# 		else:
# 			ans = mid
# 			end = mid - 1
# 	print(ans)

# if __name__ == "__main__":
# 	main()

# 수들의 합 2
# https://www.acmicpc.net/problem/2003


# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# ans = 0
# s = 0
# e = s+1

# while s<= e and e <= n:
# 	tmp = sum(arr[s:e])

# 	if tmp == m:
# 		ans+=1
# 		e+=1
# 	elif tmp < m:
# 		e+=1
# 	else:
# 		s+=1
# print(ans)




# 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# pre = [0]

# tmp = 0
# for i in arr:
# 	tmp += i
# 	pre.append(tmp)

# for i in range(m):
# 	a,b = map(int,input().split())
# 	print(pre[b]-pre[a-1])

# 보이는 점의 개수
# https://www.acmicpc.net/problem/2725
