# 카드팩의 종류는 카드 1개가 포함된 카드팩, 카드 2개가 포함된 카드팩, ... 카드 N개가 포함된 카드팩과 같이 총 N가지가 존재한다.

# 민규는 카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을 것이라는 미신을 믿고 있다.
# 민규는 돈을 최대한 많이 지불해서 카드 N개 구매하려고 한다. 카드가 i개 포함된 카드팩의 가격은 Pi원이다.

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]+list(map(int,input().split(' ')))
dp = [0] * (n+1)


for i in range(1,n+1):
	for j in range(1,i+1):
		dp[i] = max(dp[i-j] + arr[j], dp[i])

print(dp[n])


