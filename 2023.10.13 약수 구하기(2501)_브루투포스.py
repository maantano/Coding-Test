n,m = map(int,input().split())



tmp = 0
arr = []
while True:
	tmp+=1
	if tmp == n:
		break
	else:
		if n % tmp == 0:
			arr.append(tmp)
arr.append(n)


if len(arr)>=m:
	print(arr[m-1])
else:
	print(0)


N, K = map(int, input().split())
lst = []
for i in range(1, N+1) :
	if N % i == 0 :
		lst.append(i)
if len(lst) < K :	# 약수의 개수가 K보다 작을 때
	print(0)
else :
	print(lst[K-1])	# 인덱스 번호에 맞춰서 K-1번째로 해야함
