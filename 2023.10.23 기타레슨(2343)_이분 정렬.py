# import sys
# # n,m = map(int,input().split())

# n = 9
# m = 3
# # arr = list(map(int,input().split()))
# arr = list(map(int,'1 2 3 4 5 6 7 8 9'.split(' ')))
# arr.sort()

# lt = 0
# rt = n
# answer = []
# while lt <= rt:
# 	mid = (lt+rt) // 2
# 	tmpL = 0
# 	tmpR = 0
# 	for i in arr[:mid+1]:
# 		tmpL += i
# 	for j in arr[mid:]:
# 		tmpR += j
# 	print('tmpL,tmpR ====>',tmpL,tmpR)
# 	if tmpL < tmpR:
# 		answer.append(tmpL)
# 		lt = mid +1
# 	else:
# 		answer.append(tmpR)
# 		rt = mid-1
# 	print(answer)


# 9 3
# 1 2 3 4 5 6 7 8 9


N = 9
M = 3
# arr = list(map(int,input().split()))
arr = list(map(int,'1 2 3 4 5 6 7 8 9'.split(' ')))
N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
left, right = max(arr), sum(arr)
while left <= right:
    mid = (left+right)//2

    # 블루레이에 강의 넣기
    count, sum = 0, 0
    for i in range(N):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]

    if sum:
        count += 1

    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)
