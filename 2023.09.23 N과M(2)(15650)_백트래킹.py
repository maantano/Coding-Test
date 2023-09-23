
N,M = map(int,input().split())
chkList = [0] * (N+1)
answerList = []

def recur(n,smallList):
	if n == M:
		if sorted(smallList) not in sorted(answerList):
			answerList.append(smallList)
			return
	for i in range(1,N+1):
		if chkList[i] == 0:
			chkList[i] = 1
			recur(n+1,smallList+[i])
			chkList[i] = 0
recur(0,[])
for i in answerList:
	print(*i)


# MJ 풀이
# N, M = map(int,input().split())
# check_list = [0] * (N+1)
# answer_list = []

# def dfs(n, small_list):
#     if n == M:
#         answer_list.append(small_list)
#         return
#     for i in range(1,N+1):
#         if small_list[-1] > i:
#             continue
#         if check_list[i] == 0:
#             check_list[i] = 1
#             dfs(n+1,small_list+[i])
#         check_list[i] = 0

# dfs(0, [0])
# for i in answer_list:
#     i.pop(0)
#     print(*i)

