# n = int(input())

# # arr = [list(map(int,input().split())) for _ in range(1,n+1)]
# arr = [[]*(n+1) for _ in range(n+1)]
# for i in range(1,n+1):
# 	arr[i] = list(map(int,input().split()))


# 3
# 26 40 83
# 49 60 57
# 13 89 99
# # 96


# def dP():
# 	for i in range(1,n+1):
# 		for j in range(1,n+1):


n = int(input())
a = [0]*n

for i in range(n):
	a[i] = list(map(int,input().split()))

for i in range(1,n): # 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기때문이다
	a[i][0]= min(a[i-1][1],a[i-1][2]) + a[i][0]
	a[i][1]= min(a[i-1][0],a[i-1][2]) + a[i][1]
	a[i][2]= min(a[i-1][0],a[i-1][1]) + a[i][2]

print(min(a[n-1][0],a[n-1][1],a[n-1][2]))



