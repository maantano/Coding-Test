# import sys
# input = sys.stdin.readline

# from itertools import combinations_with_replacement
# a,b,c= map(int,input().split())

# arrA = [i for i in range(1,a+1)]
# arrB = [i for i in range(1,b+1)]
# arrC = [i for i in range(1,c+1)]

# s = set(arrA)
# s.update(arrB)
# s.update(arrC)

# combi = list(combinations_with_replacement(s,3))
# d = {}
# for i in combi:
# 	if sum(i) not in d:
# 		d[sum(i)] = 1
# 	else:
# 		d[sum(i)] += 1
# sd = sorted(d.items(), key= lambda x  : x[1])

# if sd[-1][1] == sd[-2][1]:
# 	print(sorted(d.items(), key= lambda x  : (x[1],-x[0]),reverse=True)[0][0])
# else:
# 	print(sd[-1][0])


s1, s2, s3 = map(int, input().split())
d = {}
for i in range(1, s1+1):
	for j in range(1, s2+1):
		for k in range(1, s3+1):
			d[i+j+k] = d.get(i+j+k, 0) + 1
li = sorted(d.items(), key=lambda x:(-x[1],x[0]))
print(li[0][0])
