targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

def solution(targets):
	targets.sort(key=lambda x : (x[1],x[0]))
	s,e = 0,0
	answer = 0
	for target in targets:
		if target[0] >= e:
			answer+=1
			e = target[1]
	return answer
solution(targets)
