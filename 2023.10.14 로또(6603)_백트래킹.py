# 로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

def bt(answer):
	if len(answer) == 6:
		print(' '.join(map(str,answer)))
		return answer

	for i in range(n):
		if not visited[i]:
			visited[i]  = 1
			bt(answer+[arr[i]])
			visited[i]  = 0

while True:
	data= list(map(int,input().split()))
	n = data[0]
	arr = data[1:]
	answer = []
	visited = [0] * (n+1)
	if n == 0:
		break
	bt(answer)





# 	for i in range()



