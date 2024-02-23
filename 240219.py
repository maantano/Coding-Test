
# # # https://www.acmicpc.net/problem/2531

# # import sys
# # input = sys.stdin.readline

# # n,d,k,c = map(int,input().split())
# # arr = [int(input()) for _ in range(n)]
# # start,end = 0, 0
# # answer = 0

# # while start != n:
# # 	end = start+k
# # 	case = set()
# # 	add = True

# # 	for i in range(start,end):
# # 		i %= n
# # 		case.add(arr[i])
# # 		if arr[i] == c: add= False
# # 	cnt = len(case)
# # 	if add : cnt += 1
# # 	answer = max(cnt,answer)
# # 	start += 1
# # print(answer)



# # 주유소
# # https://www.acmicpc.net/problem/13305

# # n = int(input())
# # dist = list(map(int,input().split()))
# # p = list(map(int,input().split()))

# # ans = dist[0] * p[0]

# # m = p[0]
# # distance = 0
# # for i in range(1,n-1):
# # 	if p[i] < m:
# # 		ans += m * distance
# # 		distance = dist[i]
# # 		m = p[i]
# # 	else:
# # 		distance += dist[i]
# # 	if i == n-2:
# # 		ans += m * distance
# # print(ans)

# # n = int(input())
# # cities = list(map(int, input().split()))
# # prices = list(map(int, input().split()))

# # ans = 0
# # min_price = prices[0]

# # for i in range(n-1):
# # 	if prices[i] < min_price:
# # 		min_price = prices[i]

# # 	ans += min_price * cities[i]

# # print(ans)


# # 카드 정렬하기
# # https://www.acmicpc.net/problem/1715

# # import sys
# # input = sys.stdin.readline

# # import heapq

# # n = int(input())
# # cards = []
# # for i in range(n):
# # 	heapq.heappush(cards,int(input()))
# # total = 0

# # while len(cards) > 1:
# # 	a = heapq.heappop(cards)
# # 	b = heapq.heappop(cards)
# # 	heapq.heappush(cards,a+b)

# # 	total += a+b
# # print(total)



# # n = int(input())
# # arr = sorted([int(input()) for _ in range(n)])
# # if n <= 1:
# # 	print(arr[0])
# # elif n == 2:
# # 	print(arr[0]+arr[1])
# # else:
# # 	ans = arr[0]+arr[1]
# # 	start = 2
# # 	while start <= n-1:
# # 		ans+= (arr[start]+ans)
# # 		start+=1
# # 	print(ans)



# # 두 수의 합
# # https://www.acmicpc.net/problem/3273



# # n = int(input())
# # arr = sorted(list(map(int,input().split())))
# # x = int(input())

# # start = 0
# # end = n-1
# # ans = 0

# # while start < end:
# # 	tmp = arr[start] + arr[end]
# # 	if tmp == x:
# # 		ans+=1
# # 	if tmp > x:
# # 		end -= 1
# # 	else:
# # 		start+=1
# # print(ans)


# # 키로거
# # https://www.acmicpc.net/problem/5397


# # n = int(input())
# # for _ in range(n):
# # 	left = []
# # 	right = []
# # 	cmd = input()

# # 	for i in cmd:
# # 		if i == '<':
# # 			if left:
# # 				right.append(left.pop())
# # 		elif i == '>':
# # 			if right:
# # 				left.append(right.pop())
# # 		elif i == '-':
# # 			if left:
# # 				left.pop()
# # 		else:
# # 			left.append(i)
# # 	left.extend(reversed(right))

# # 	print(''.join(left))


# # 요세푸스 문제
# # https://www.acmicpc.net/problem/1158

# # n,k = map(int,input().split())
# # chk = [i for i in range(1,n+1)]

# # s1 = []
# # idx = 0

# # while len(chk):
# # 	idx += k-1
# # 	if idx >= len(chk):
# # 		idx %= len(chk)
# # 	s1.append(chk.pop(idx))
# # print('<',", ".join(map(str, s1)),'>',sep='')



# # 알파벳 개수
# # https://www.acmicpc.net/problem/10808

# # string = input()
# # chk = [0] * 26
# # for s in string:
# # 	chk[ord(s) - ord('a')] +=1
# # print(*chk)


# # 개수 세기
# # https://www.acmicpc.net/problem/10807

# # n = int(input())
# # arr = list(map(int,input().split()))
# # chk = int(input())
# # d = {}

# # for i in range(n):
# # 	if arr[i] in d:
# # 		d[arr[i]]+=1
# # 	else:
# # 		d[arr[i]] = 1
# # if chk in d:
# # 	print(d[chk])
# # else:
# # 	print(0)

# # 방 배정
# # https://www.acmicpc.net/problem/13300

# # 0 : 여
# # 1 : 남
# # n,k = map(int,input().split())
# # male = [0] * 6
# # female = [0] * 6
# # for i in range(n):
# # 	s,g = map(int,input().split())
# # 	if s:
# # 		male[g-1]+=1
# # 	else:
# # 		female[g-1]+=1
# # total = 0
# # for i in range(6):
# # 	if male[i] % k > 0:
# # 		total+= 1
# # 	total+= male[i] // k
# # 	if female[i] % k > 0:
# # 		total+= 1
# # 	total+= female[i] // k
# # print(total)


# # Strfry
# # https://www.acmicpc.net/problem/11328

# # N = int(input())

# # for i in range(N):
# # 	a, b = input().split()
# # 	a = ''.join(sorted(a))
# # 	b = ''.join(sorted(b))

# # 	if len(a) != len(b):
# # 		print("Impossible")
# # 		continue

# # 	for i in range(len(a)):
# # 		if a[i] != b[i]:
# # 			flag = False
# # 			break
# # 		else:
# # 			flag = True

# # 	if flag:
# # 		print("Possible")
# # 	else:
# # 		print("Impossible")




# # 애너그램 만들기
# # https://www.acmicpc.net/problem/1919

# # 틀림
# # s1 = input()
# # s2 = input()
# # d1 = {}
# # d2 = {}

# # for s in s1:
# # 	if s in d1:
# # 		d1[s] +=1
# # 	else:
# # 		d1[s] = 1
# # for s in s2:
# # 	if s in d2:
# # 		d2[s] +=1
# # 	else:
# # 		d2[s] = 1
# # ans = 0
# # for i in d1:
# # 	if i not in d2:
# # 		ans+= d1[i]
# # for i in d2:
# # 	if i not in d1:
# # 		ans+= d2[i]
# # print(ans)


# # 맞음
# # alpha = [0]* 26

# # a = list(input())
# # b = list(input())

# # for i in a:
# # 	alpha[ord(i)-97] += 1
# # for j in b:
# # 	alpha[ord(j)-97] -= 1
# # ans = 0
# # for i in alpha:
# # 	if i != 0:
# # 		ans+=abs(i)
# # print(ans)


# # 에디터
# # https://www.acmicpc.net/problem/1406



# # string = list(input().strip())
# # n = int(input())
# # idx = len(string)
# # for i in range(n):
# # 	p = input().split()
# # 	if p[0] == 'P':
# # 		if idx < len(string):
# # 			string = string[:idx] + [p[1]] + string[idx:]
# # 		else:
# # 			string.append(p[1])
# # 		idx += 1
# # 	elif p[0] == 'L' and idx > 0:
# # 		idx -= 1
# # 	elif p[0] == 'B' and idx > 0:
# # 		idx -= 1
# # 		if idx < len(string):
# # 			string = string[:idx] + string[idx + 1:]
# # 	elif p[0] == 'D' and idx < len(string):
# # 		idx += 1
# # print(''.join(string))



# # import sys

# # st1 = list(sys.stdin.readline().rstrip())
# # st2 = []

# # for _ in range(int(sys.stdin.readline())):
# # 	command = list(sys.stdin.readline().split())
# # 	if command[0] == 'L':
# # 		if st1:
# # 			st2.append(st1.pop())

# # 	elif command[0] == 'D':
# # 		if st2:
# # 			st1.append(st2.pop())

# # 	elif command[0] == 'B':
# # 		if st1:
# # 			st1.pop()

# # 	else:
# # 		st1.append(command[1])

# # st1.extend(reversed(st2))
# # print(''.join(st1))


# # 거스름돈
# # https://www.acmicpc.net/problem/14916

# # n = int(input())
# # ans = 0
# # while True:
# # 	if n % 5 == 0:
# # 		ans += n //5
# # 		break
# # 	else:
# # 		n-=2
# # 		ans+=1
# # 	if n <0:
# # 		break
# # if n <0:
# # 	print(-1)
# # else:
# # 	print(ans)


# # 수리공 항승
# # https://www.acmicpc.net/problem/1449

# # n,l = map(int,input().split())
# # arr = sorted(list(map(int,input().split())))

# # visited = [0] * n
# # start = arr[0]
# # count = 1

# # for i in arr[1:]:
# # 	if i in range(start,start+l):
# # 		continue
# # 	else:
# # 		start = i
# # 		count+=1
# # print(count)


# # 강의실 배정
# # https://www.acmicpc.net/problem/11000
# import heapq

# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# arr.sort(key=lambda x : (x[0],x[1]))

# hq = [arr[0][1]]

# for i in range(1,n):
# 	if hq[0] <= arr[i][0]:
# 		heapq.heappop(hq)
# 	heapq.heappush(hq,arr[i][1])
# print(len(hq))


