import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
	x,y = map(int,input().split())
	arr.append([x,y])

ans = 0
def dfs(n,cnt):
	global ans
	if ans >=(cnt+(N-n)*2):
		# 남은 횟수 (N -n) 동안 양쪽 계산 모두 깨질 경우 * 2 + 지금까지 깬 계란 갯수 cnt를 더한 값보다 ans가 크다면 더 체크할 필요가 없다.
		return

	if n == N: # 끝내는 조건 끝꺼지 다 돌았을때
		ans = max(ans,cnt)
		return

	if arr[n][0]<= 0: # 내 계란이 이미 꺠진 경우 그냥 다음 계란으로 넘어감
		dfs(n+1,cnt)
	else:
		flag = False # 부딪히지 않은 경우, 남은 멀쩡한 계란이 없을때 모두 깨져 있거나, 내가 든 계란이거나
		for i in range(N):
			if n == i or arr[i][0] <= 0: # 내가 든 계란이거나, 이미 깨진 계란이거나 하면 continue
				continue
			flag = True
			arr[n][0] -= arr[i][1]
			arr[i][0] -= arr[n][1]
			dfs(n+1, cnt + int(arr[n][0] <= 0) + int(arr[i][0] <= 0))
			arr[n][0] += arr[i][1]
			arr[i][0] += arr[n][1]
		if not flag:
			dfs(n+1,cnt)  # 남은 멀쩡한 계란이 없을때 모두 깨져 있거나, 내가 든 계란이여서 엔드조건을 향해서 감
dfs(0,0)
print(ans)
