
N,M = map(int,input().split())
chkList = [0] * (N+1)
answerList = []

def recur(n,smallList):
	if n == M:
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


import sys
input = sys.stdin.readline

def backtracking():
    if len(array) == m:
        print(" ".join(map(str, array)))
        return

    for i in range(1, n+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()

n, m = map(int,input().split())
array = []

backtracking()
