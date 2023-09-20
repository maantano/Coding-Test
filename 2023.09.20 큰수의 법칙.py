# n=5
# m=8
# k=3
# arr = [2,4,5,4,6]

n,m,k = int(map(input().split()))
arr = list(map(int,input().split()))

# 내 풀이
answer = 0
arr.sort(reverse=True)
cnt = 0
for i in range(m):
	if cnt == k:
		answer += arr[1]
		cnt =0
	else:
		answer += arr[0]
	cnt+=1
print(answer)



# 책 풀이
arr.sort()
first = arr[n-1]
second = arr[n-2]
answer = 0
while True:
	for i in range(k):
		if m == 0:
			break
		answer += first
		m -=1
	if m ==0:
		break
	answer += second
	m -=1
print(answer)
