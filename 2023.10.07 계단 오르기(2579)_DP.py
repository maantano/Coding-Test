# 계단 오르는 데는 다음과 같은 규칙이 있다.

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
# 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다.
# 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.


n = int(input())
arr = [0] * 301
for i in range(n):
	arr[i] = (int(input()))

d = [0] * 301
d[0] = arr[0]
d[1] = arr[1]+arr[0]
d[2] = max((arr[0]+arr[2]),(arr[1]+arr[2]))

for i in range(3,n):
	d[i] = max(d[i-3]+arr[i-1]+arr[i],d[i-2]+arr[i])
print(d[n-1])


N = int(input())
stair = [0]*301
for i in range(N):
    stair[i]=int(input())

DP = [0]*301
DP[0] = stair[0]
DP[1] = stair[0]+stair[1]
DP[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, N):
    DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2]+stair[i])

print(DP[N-1])

# https://chanos.tistory.com/entry/%EB%B0%B1%EC%A4%80-2579%EB%B2%88-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4
