# # 바이러스가 숙주의 몸속에서 1초당 P배씩 증가한다.
# # 처음에 바이러스 K마리가 있었다면 N초 후에는 총 몇 마리의 바이러스로 불어날까? N초 동안 죽는 바이러스는 없다고 가정한다.

import sys
input = sys.stdin.readline

k,p,n = map(int,input().split())
# 2 3 2

result = k
for i in range(n):
	a = result % 1000000007
	b = p % 1000000007
	result = (a*b) % 1000000007
print(result)

# 모듈러 산술
# https://sskl660.tistory.com/75
