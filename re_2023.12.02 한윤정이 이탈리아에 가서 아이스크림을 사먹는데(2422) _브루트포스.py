import sys
iinput = sys.stdin.readline

n,m = map(int,input().split())
ice = [i for i in range(1,n+1)]
skip = [list(map(int,input().split())) for _ in range(m)]

from itertools import combinations

all = list(combinations(ice,m))
cnt = 0
for chk in all:
	flag = True
	for a,b in skip:
		if a in chk and b in chk:
			flag = False
			continue
	if flag:
		print(chk)
		cnt+=1
print(cnt)




# import sys
# from itertools import combinations

# input = sys.stdin.readline

# n, m = map(int, input().split())
# ice = [[False for _ in range(n)] for _ in range(n)]
# for i in range(m):
# 	i1, i2 = map(int, input().split())
# 	ice[i1 - 1][i2 - 1] = True
# 	ice[i2 - 1][i1 - 1] = True

# result = 0

# for i in combinations(range(n), 3):
# 	if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
# 		continue
# 	result += 1
# print(result)



# # from itertools import combinations,permutations,combinations_with_replacement
# # combi = list(combinations(range(1,n+1),m))
# # # for chk in list(combinations(range(1,n+1),m)):
# # cnt = 0
# # for chk in combi:
# # 	for i in skip:
# # 		for j in i:
# # 			if j in chk:
# # 				break
# # 			cnt+=1





# # # print(i for i in range(4))
# # print(cnt)
