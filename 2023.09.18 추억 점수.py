
name=["may", "kein", "kain", "radi"]
yearning=[5, 10, 1, 3]
photo=[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
# result = [19, 15, 6]

def solution(name,yearning,photo):
	answer = []
	d = dict(zip(name,yearning))
	for i in photo:
		cnt = 0
		for j in i:
			if j in name:
				cnt += d[j]
		answer.append(cnt)
	return answer


solution(name,yearning,photo)
