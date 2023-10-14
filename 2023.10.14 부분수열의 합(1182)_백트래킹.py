# import sys
# input = sys.stdin.readline

# n,s = map(int,input().split())
# arr = list(map(int,input().split()))

# visit = [ False for _ in range(n)]
# result = 0
# cnt = 0
# def bt(idx):
# 	global result
# 	for i in range(n):
# 		result = arr[i]
# 		for j in range(idx,n):
# 			if not visit[j]:
# 				result+=arr[j]
# 				if result == s:
# 					cnt+=1
# 				visit[i] = True
# 				bt(j)
# 				visit[i] = False

# bt(0)
# print(cnt)


import sys


# 백트래킹 함수
def back_tracking(idx, res):
	global cnt

	# 현재 idx가 정수의 개수보다 크면 리턴
	if idx >= n:
		return

	# 수열에 현재 idx 정수를 더한다.
	res += k[idx]

	# 현재 수열이 s라면 카운트
	if res == s:
		cnt += 1
	print('idx,res =====>',idx,' =====>',res)
	back_tracking(idx + 1, res) # 현재 idx 정수를 더한 것
	back_tracking(idx + 1, res - k[idx]) # 현재 idx 정수를 더하지 않은 것(백트래킹)


n, s = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))
cnt = 0

back_tracking(0, 0)
print(cnt)
