N,M = map(int,input().split())
chkList = [0] * (N+1)
answerList = []

def bt(n,smallList):
	if n == M:
		answerList.append(smallList)
		return
	for i in range(1,N+1):
		if chkList[i] == 0:
			chkList[i] = 1
			bt(n+1,smallList+[i])
			chkList[i] = 0
bt(0,[])

for i in answerList:
	print(*i)
