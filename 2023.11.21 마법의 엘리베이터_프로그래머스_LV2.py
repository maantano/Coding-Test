
storey = 16
# storey = 2554

result = 6
# result = 16

def solution(storey):
	answer = 0
	cnt = len(str(storey))
	for i in range(cnt):
		if int(str(storey)[::-1][i]) >5:
			answer+=10-(int(str(storey)[::-1][i]))
		else:
			answer+=int(str(storey)[::-1][i])
	print(answer)
	return answer

solution(storey)
