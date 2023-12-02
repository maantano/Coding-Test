import sys
input = sys.stdin.readline

start = int(input())
dp = [[start] for _ in range(start+1)]
maxIdx = []
for i in range(1,start+1):
	cnt = 0
	tmp = i
	while True:
		if tmp < 0:
			if len(dp[i]) > len(maxIdx):
				maxIdx = dp[i]
			break
		else:
			dp[i].append(tmp)
			tmp = dp[i][cnt] - dp[i][-1]
			cnt+=1
print(len(maxIdx))
print(*maxIdx)

