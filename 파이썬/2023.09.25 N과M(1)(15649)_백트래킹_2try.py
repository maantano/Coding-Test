N,M = map(int,input().split())
chk = [0] * (N+1)
answerList = []


def bt(n,smallList):
	if n == M:
		answerList.append(smallList)
		return
	for i in range(1,N+1):
		if chk[i] == 0:
			chk[i] = 1
			bt(n+1,smallList+[i])
			chk[i] = 0
bt(0,[])
for i in answerList:
	print(*i)
