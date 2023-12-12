# n = int(input())

# dp = [int(1e9)]*(n+1)


# for i in range(3,len(dp)):
# 	dp[i] = min(dp[i-1]+i,i//3,i//5)
# print(dp)
# print(dp[n]+1)


sugar = int(input())

bag = 0
while sugar >= 0 :
	if sugar % 5 == 0 :  # 5의 배수이면
		bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
		print(bag)
		break
	sugar -= 3
	bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
	print(-1)
