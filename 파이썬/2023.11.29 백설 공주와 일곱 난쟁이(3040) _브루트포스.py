# import sys
# from itertools import combinations

# input=sys.stdin.readline

# def solve(case):
# 	if sum(case)==100:
# 		case=list(case)
# 		case.sort()
# 		for i in case:
# 			print(int(i))
# 		return True
# 	return False


# if __name__ == "__main__":
# 	data=set()  #집합 자료형
# 	for i in range(9):
# 		height=int(input().strip())
# 		data.add(height)

# 	for case in combinations(data,7):
# 		if solve(case):
# 			break


# import sys; input = sys.stdin.readline
# from itertools import combinations

# dwarves = [int(input()) for _ in range(9)]
# total = sum(dwarves)
# rm_v1, rm_v2 = None, None
# for v1, v2 in combinations(dwarves, 2):
# 	if total - v1 - v2 == 100:
# 		rm_v1, rm_v2 = v1, v2
# 		break
# dwarves.remove(rm_v1)
# dwarves.remove(rm_v2)
# print(*dwarves, sep="\n")




arr = [int(input()) for _ in range(9)]

for i in range(9):
	for j in range(1,9):
		if sum(arr) - arr[i] - arr[j] == 100:
			x,y = arr[i],arr[j]
			break
arr.remove(x)
arr.remove(y)
for i in arr:
	print(i)

