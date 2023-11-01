
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(input().rstrip()) for _ in range(n)]


def chk(arr):
	mCnt = 1
	for i in range(n):
		cnt = 1
		for j in range(1,n):
			if arr[i][j] == arr[i][j-1]:
				cnt+=1
			else:
				cnt = 1
			mCnt = max(mCnt,cnt)
		cnt = 1
		for j in range(1,n):
			if arr[j][i] == arr[j-1][i]:
				cnt+=1
			else:
				cnt = 1
			mCnt = max(mCnt,cnt)
	return mCnt


ans = 0
for i in range(n):
	for j in range(n):
		if j + 1 < n:
			arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
			cnt = chk(arr)
			ans = max(cnt,ans)
			arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]

		if i + 1 < n:
			arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
			cnt = chk(arr)
			ans = max(cnt,ans)
			arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]

print(ans)
