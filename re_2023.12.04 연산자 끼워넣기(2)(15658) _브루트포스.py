import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
unitl = list(map(int,input().split()))
ans_max = -1000000001
ans_min = 1000000001

def unit(total,idx):
	global ans_max,ans_min
	if idx == n-1:
		ans_min = min(ans_min,total)
		ans_max = max(ans_max,total)
		return
	for i in range(4):
		if unitl[i] != 0:
			unitl[i] -= 1
			if i == 0:
				unit(total+arr[idx+1],idx+1)
			elif i == 1:
				unit(total-arr[idx+1],idx+1)
			elif i == 2:
				unit(total*arr[idx+1],idx+1)
			else:
				unit(int(total/arr[idx+1]),idx+1)
			unitl[i] += 1
unit(arr[0],0)
print(ans_max)
print(ans_min)



# from itertools import combinations_with_replacement,combinations,permutations

# from collections import Counter
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))
# unit = list(map(int,input().split()))
# plus,minus,multi,divide = unit[0],unit[1],unit[2],unit[3]
# unitd = {'+':plus,'-':minus,'*':multi,'//':divide}
# unitl = ['+','-','*','//']
# combi = list(permutations(unitl,n-1))

# for i in combi:
# 	counter = Counter(i)
# 	if counter['+'] > unitd['+'] or counter['-'] > unitd['-'] or counter['*'] > unitd['*'] or counter['//'] > unitd['//']:
# 		combi.remove(i)


# for i in range(len(combi)):
# 	print(''.join(combi[i]))


