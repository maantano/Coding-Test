
N,M = map(int,input().split())
chkList = [0] * (N+1)
answerList = []

def recur(n,smallList):
	if n == M:
		answerList.append(smallList)
		return
	for i in range(1,N+1):
		recur(n+1,smallList+[i])

recur(0,[])
for i in answerList:
	print(*i)


# def back(cnt, N, M):
#     if cnt == M:
#         print(*result)
#         return

#     for i in range(N):
#         result[cnt] = arr[i]
#         back(cnt + 1, N, M)

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = [i for i in range(1, N + 1)]

# result = [0] * M
# back(0, N, M)
