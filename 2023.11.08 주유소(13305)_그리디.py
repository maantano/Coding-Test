import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

mini = price[0]
answer = 0

for i in range(n-1):
	if mini > price[i]:
		mini = price[i]
	answer+=(mini * distance[i])
print(answer)



