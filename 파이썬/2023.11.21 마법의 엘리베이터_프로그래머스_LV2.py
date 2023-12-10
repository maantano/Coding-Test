
storey = 16
# storey = 2554
result = 6
# result = 16

# def solution(storey):
# 	answer = 0
# 	cnt = len(str(storey))
# 	for i in range(cnt):
# 		if int(str(storey)[::-1][i]) >5:
# 			answer+=10-(int(str(storey)[::-1][i]))
# 		else:
# 			answer+=int(str(storey)[::-1][i])
# 	print(answer)
# 	return answer

# solution(storey)


def solution(storey):
	answer = 0
	while storey >= 1:
		n = storey % 10

		if n >5:
			answer += (10-n)
			storey += (10-n)
		elif n <5:
			answer += n
			storey -= n
		else:
			tmpStorey = storey // 10
			if tmpStorey % 10 >=5:
				answer+=(10-n)
				storey+=(10-n)
			else:
				answer+=n
				storey-=n
		storey //= 10

	return answer
