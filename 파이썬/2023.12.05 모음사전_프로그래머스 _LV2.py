# import sys
# input = sys.stdin.readline
# from itertools import combinations_with_replacement
# chk = ['A', 'E', 'I', 'O', 'U']

# # combi =  list(''.join(x) for x in list(combinations_with_replacement(chk,5)))
# s = []
# for i in range(len(chk)):
# 	s.extend(''.join(x) for x in list(combinations_with_replacement(chk,i)))

# print

from itertools import product
def solution(word):
	answer = []
	li = ['A', 'E', 'I', 'O', 'U']
	for i in range(1,6):
		for per in product(li,repeat = i):
			answer.append(''.join(per))
	answer.sort()
	print(answer.index(word)+1)



def solution2(word):
	answer = 0
	dic = ['A', 'E', 'I', 'O', 'U']
	li = [5**i for i in range(len(dic))]

	for i in range(len(word)-1,-1,-1):
		idx = dic.index(word[i])
		for j in range(5-i):
			answer += li[j]*idx
		answer+=1
	return answer

word = ["AAAAE","AAAE","I","EIO"]
for i in word:
	solution2(i)
