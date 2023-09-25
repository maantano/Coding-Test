
N,M = map(int,input().split())
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


from itertools import product

list1 = list(i for i in range(1,N+1))

for i in product(list1,list1, repeat=1):
	print(*i)
