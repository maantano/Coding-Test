# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.


# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

# 5
# 2 4 -10 4 -9

# 2 3 0 3 1

# 6
# 1000 999 1000 999 1000 999

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))

# visited = [0] * n

# for i in range(len(arr)):
# 	for j in range(len(arr)):
# 		if arr[i] > arr[j]:
# 			visited[i]+=1

# print(*visited)


# import sys
# input = sys.stdin.readline

# n = int(input())

# arr = list(map(int, input().split()))
# arr2 = sorted(list(set(arr)))

# for i in arr:
# 	print(arr2.index(i), end = ' ')



import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
	print(dic[i], end = ' ')
