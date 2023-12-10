# k = 6
# tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
# k = 4
# tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
result = 6

# def solution(k, tangerine):
# 	d = {}
# 	for t in tangerine:
# 		if t not in d:
# 			d[t] = 1
# 		else:
# 			d[t] += 1
# 	chk = sorted(d.items(),key=lambda x : x[1],reverse=True)
# 	answer = 0
# 	cnt = 0
# 	for i in chk:
# 		if cnt + i[1] < k:
# 			cnt += i[1]
# 			answer += 1
# 		elif cnt +i[1] == k:
# 			return answer+1
# 		else:
# 			return answer +1
# 	return answer

# print(solution(k, tangerine))


from collections import Counter
def solution(k, tangerine):
	answer = 0
	counter = Counter(tangerine)

	sort_ = sorted(counter.items(),key=lambda x :x[1],reverse=True)

	for i in sort_:
		dk,dv = i
		if k > dv:
			k-=dv
			answer+=1
		else:
			return answer+1
	return answer




print(solution(k, tangerine))
