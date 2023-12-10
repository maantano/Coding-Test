# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.

import sys
input = sys.stdin.readline

n,k = map(int,input().split())

arr = sorted([int(input()) for _ in range(n)],reverse=True)

cnt = 0
for i in arr:
	cnt += int(k // i)
	k = k % i
print(cnt)


