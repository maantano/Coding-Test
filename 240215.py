# 숫자 카드
# https://www.acmicpc.net/problem/10815
# n = int(input())
# sang = sorted(map(int,input().split()))
# m = int(input())
# chk = map(int,input().split())

# for c in chk:
# 	start = 0
# 	end = n-1
# 	ok = False
# 	while start <= end:
# 		mid = (start+end) // 2
# 		if c == sang[mid]:
# 			ok = True
# 			break
# 		if c > sang[mid]:
# 			start = mid+ 1
# 		elif c < sang[mid]:
# 			end = mid -1
# 	print(1 if ok else 0,end = ' ')



# 수 찾기
# https://www.acmicpc.net/problem/1920

# n = int(input())
# arr = sorted(list(map(int,input().split())))
# m = int(input())
# chks = list(map(int,input().split()))

# for chk in chks:
# 	ok = False
# 	start,end = 0,n-1
# 	while start <= end:
# 		mid = (start+end) // 2

# 		if arr[mid] == chk:
# 			ok = True
# 			break
# 		if arr[mid] > chk:
# 			end = mid -1
# 		elif arr[mid] < chk:
# 			start = mid + 1

# 	print(1 if ok else 0)

# 숫자 카드 2
# https://www.acmicpc.net/problem/10816

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n = int(input())
# arr = list(map(int,input().split()))
# m = int(input())
# chks = list(map(int,input().split()))
# # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
# # print(arr)

# d = {}
# for i in arr:
# 	if i in d:
# 		d[i] += 1
# 	else:
# 		d[i] = 1
# print(' '.join(str(d[chk]) if chk in d else '0' for chk in chks))



# n = int(input())
# arr = sorted(list(map(int,input().split())))
# m = int(input())
# chks = list(map(int,input().split()))


# def bin(chk,arr,start,end):
# 	if start > end:
# 		return 0

# 	mid = (start+end) // 2
# 	if chk == arr[mid]:
# 		return arr[start:end+1].count(chk)
# 	if chk < arr[mid]:
# 		return bin(chk,arr,start,mid-1)
# 	elif chk > arr[mid]:
# 		return bin(chk,arr,mid+1,end)

# d = {}

# for i in chks:
# 	if i not in d:
# 		d[i] = bin(i,arr,0,n-1)

# print(' '.join(str(d[chk]) if chk in d else 0 for chk in chks ))



# 나무 자르기
# https://www.acmicpc.net/problem/2805

# n,m = map(int,input().split())
# tree = sorted(list(map(int,input().split())))
# start,end = 1,max(tree)
# while start <= end:
# 	mid = (start+end) // 2
# 	total = 0
# 	for i in tree:
# 		if i >= mid:
# 			total += i-mid
# 	if total >= m:
# 		start = mid+1
# 	else:
# 		end = mid - 1
# print(end)



# 랜선 자르기
# https://www.acmicpc.net/problem/1654

# k,n = map(int,input().split())
# line = [int(input()) for _ in range(k)]

# start,end = 1,max(line)

# while start<=end:
# 	mid = (start+end) // 2
# 	l = 0
# 	for i in line:
# 		l += i //mid
# 	if l >= n:
# 		start = mid+1
# 	else:
# 		end = mid-1
# print(end)


# 예산
# https://www.acmicpc.net/problem/2512

# n = int(input())
# arr = sorted(list(map(int,input().split())))
# total = int(input())

# start,end = 0,max(arr)

# while start<=end:
# 	mid = (start+end) // 2
# 	limit = 0
# 	for i in arr:
# 		if i < mid:
# 			limit+=i
# 		else:
# 			limit += mid

# 	if limit <= total:
# 		start = mid + 1
# 	else:
# 		end = mid - 1

# print(end)


# 게임
# https://www.acmicpc.net/problem/1072


# x,y = map(int,input().split())
# z = (100*y) // x

# left = 0
# right = x
# res = x

# if z >= 99:
# 	print(-1)

# else:
# 	while left <= right:
# 		mid = (left+right) // 2
# 		if (100*(y+mid)) // (x+mid) > z:
# 			res = mid
# 			right = mid-1
# 		else:
# 			left = mid + 1
# 	print(res)

# 기타 레슨
# https://www.acmicpc.net/problem/2343

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# start = max(arr)
# end = sum(arr)
# while start <= end:
# 	mid = (start+end) // 2
# 	total = 0
# 	count = 1
# 	for t in arr:
# 		if total + t > mid:
# 			count += 1
# 			total = 0
# 		total += t
# 	if count <= m:
# 		ans = mid
# 		end = mid - 1
# 	else:
# 		start = mid +1
# print(ans)

# 용액
# https://www.acmicpc.net/problem/2467


# n = int(input())
# arr = list(map(int,input().split()))

# start = 0
# end = n-1
# s = abs(arr[start]+arr[end])
# ansS = 0
# ansE = n-1

# while start < end:
# 	mid = arr[start]+arr[end]

# 	if abs(mid) <= s:
# 		s = abs(mid)
# 		ansS = start
# 		ansE = end
# 		if s == 0:
# 			break
# 	if mid < 0:
# 		start += 1
# 	else:
# 		end -= 1
# print(arr[ansS],arr[ansE])



# n = int(input())
# arr = list(map(int,input().split()))

# ans = float("INF")
# ansS = 0
# ansE = 0

# for i in range(n-1):
# 	cur = arr[i]
# 	start = i+1
# 	end = n-1

# 	while start <= end:
# 		mid = (start+end) // 2
# 		tmp = cur + arr[mid]

# 		if abs(tmp) < ans:
# 			ans = abs(tmp)
# 			ansS = i
# 			ansE = mid

# 			if tmp == 0:
# 				break
# 		if tmp < 0:
# 			start = mid +1
# 		else:
# 			end = mid -1

# print(arr[ansS],arr[ansE])


# 이해 안됨
# 개똥벌레
# https://www.acmicpc.net/problem/3020

# n,h = map(int,input().split())

# down = [0] * (h+1)
# up = [0] * (h+1)

# min_cnt = n
# range_cnt = 0

# for i in range(n):
# 	if i % 2 == 0:
# 		down[int(input())] += 1
# 	else:
# 		up[int(input())] += 1

# for i in range(h-1,0,-1):
# 	down[i] += down[i+1]
# 	up[i] += up[i+1]

# for i in range(1,h+1):
# 	if min_cnt > (down[i] + up[h-i+1]):
# 		min_cnt = (down[i] +  up[h-i+1])
# 		range_cnt = 1
# 	elif min_cnt == (down[i] + up[h - i + 1]):
# 		range_cnt += 1
# print(min_cnt,range_cnt)

# 좋다
# https://www.acmicpc.net/problem/1253

# n = int(input())
# arr = sorted(list(map(int,input().split())))
# cnt = 0

# start = 0
# end = n-1
# ans = []

# for i in range(n):
# 	cur = arr[i]
# 	start = 0
# 	end = n-1

# 	while start < end:
# 		tmp = arr[start] + arr[end]
# 		if tmp == cur:
# 			if start == i:
# 				start+=1
# 			elif end == i:
# 				end -=1
# 			else:
# 				cnt+=1
# 				break
# 		elif tmp > cur:
# 			end -=1
# 		else:
# 			start += 1
# print(cnt)

# 시간 초과
# import sys
# input = sys.stdin.readline
# def chk(n):
# 	for i in range(2,int(n**0.5)+1):
# 		if n % i == 0:
# 			return False
# 	return True

# def chk2(n):
# 	idx = len(str(n)) // 2
# 	if len(str(n)) % 2 ==0:
# 		if str(n)[:idx] == str(n)[idx:][::-1]:
# 			return True
# 		else:
# 			return False
# 	else:
# 		if str(n)[:idx] == str(n)[idx+1:][::-1]:
# 			return True
# 		else:
# 			return False

# def chk3(n):
# 	if str(n)  == str(n)[::-1]:
# 		return True
# 	else:
# 		return False

# n = int(input())
# ans = 0
# while True:
# 	if n == 1:
# 		continue
# 	if chk(n) and chk3(n):
# 		ans = n
# 		break
# 	n+=1

# print(ans)


# # 통과
# import math

# def isPrime(x):
# 	for i in range(2, int(math.sqrt(x)+1)):
# 		if x % i == 0:
# 			return False
# 	return True

# N = int(input())
# result = 0

# for i in range(N, 1000001):
# 	if i == 1:
# 		continue
# 	if str(i) == str(i)[::-1]:
# 		if isPrime(i) == True:
# 			result = i
# 			break

# if result == 0:
# 	result = 1003001

# print(result)
