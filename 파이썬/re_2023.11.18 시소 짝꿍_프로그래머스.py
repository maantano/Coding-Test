
from collections import Counter

weights = [100,180,360,100,270]

def solution(weights):
	answer = 0

	# 1:1
	counter = Counter(weights)
	for k,v in counter.items():
		if v>=2:
			answer+= v*(v-1)//2
	weights = set(weights)

	# 2:3 2:4 3:4 비율 가지면 짝궁 가능함
	for w in weights:
		if w*2/3 in weights:
			answer+= counter[w*2/3] * counter[w]
		if w*2/4 in weights:
			answer+= counter[w*2/4] * counter[w]
		if w*3/4 in weights:
			answer+= counter[w*3/4] * counter[w]
	return answer




from collections import defaultdict

def solution(weights):
	answer = 0
	length = len(weights)
	weight_dict = defaultdict(int)

	for weight in weights :
		weight_dict[weight] += 1

	for key, val in weight_dict.items() :
		if val > 1 :
			answer += val * ( val - 1) // 2
		if key*2 in weight_dict :
			answer += val * weight_dict[key*2]
		if key*3 % 2 == 0 and key*3 // 2 in weight_dict :
			answer += val * weight_dict[key*3 // 2]
		if key*4 % 3 == 0 and key*4 // 3 in weight_dict :
			answer += val * weight_dict[key*4 // 3]

	return answer


# def solution(weights):
# 	s = set()
# 	for i in range(len(weights)):
# 		for j in range(i+1,len(weights)):
# 			a = weights[i] // gcd(weights[i],weights[j])
# 			b = weights[j] // gcd(weights[i],weights[j])
# 			if a+b <= 7:
# 				s.add((a,b))
# 	return len(s)
# print(solution(weights))



# from itertools import combinations
# def solution(weights):

# 	combi = combinations(weights,2)
# 	answer= 0
# 	for i in combi:
# 		if i[0] // gcd(i[0],i[1]) <=4 and i[1] // gcd(i[0],i[1])<=4:
# 			answer+=1
# 	return answer
# solution(weights)
