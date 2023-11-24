relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
result = 2

from itertools import combinations

# def solution(relation):
# 	d = {}
# 	for i in relation:
# 		for j in range(1,len(i)+1):
# 			for k in list(combinations(i,j)):
# 				c = ''.join(list(k))
# 				# print('c ===>',c)
# 				if str(c) not in d:
# 					d[str(c)] = 1
# 				else:
# 					d[str(c)] = d[str(c)]+1
# 	print(set(d))

# 	answer = 0
# 	return answer

def solution(relation):
	row = len(relation)
	col = len(relation[0])

	candi = []
	for i in range(1,col+1):
		candi.extend(combinations(range(col),i))
	print(candi)

solution(relation)


