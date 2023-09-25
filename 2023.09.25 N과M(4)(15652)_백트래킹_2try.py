
# N,M = map(int,input().split())
# chkList = [0] * (N+1)
# answerList = []

# def recur(n,smallList):
# 	if n == M:
# 		answerList.append(smallList)
# 		return
# 	for i in range(1,N+1):
# 		if i < smallList[-1]:
# 			continue
# 		recur(n+1,smallList+[i])

# recur(0,[0])
# for i in answerList:
# 	i.pop(0)
# 	print(*i)



N, M = map(int,input().split())
chk = [0] * (N+1)
answer = []
def bt(n,smallList):
	if n == M:
		answer.append(smallList)
		return
	for i in range(1,N+1):
		if i < smallList[-1]:
			continue
		bt(n+1,smallList+[i])
bt(0,[0])
print(answer)
for i in answer:
	i.pop(0)
	print(*i)

