
topping	= [1, 2, 1, 3, 1, 4, 1, 2]
result=2
# topping	= [1, 2, 3, 1, 4]
# result=0

# from collections import Counter
# def solution(topping):
# 	for i in range(1,len(topping)-1):
# 		if len(set(Counter(topping[i:]).keys())) == len(set(Counter(topping[:i]).keys())):
# 			answer+=1
# 	return answer

# solution(topping)


from collections import Counter
def solution(topping):
	chulsoo = Counter(topping)
	brother = set()

	answer = 0

	for i in topping:
		chulsoo[i] -= 1
		brother.add(i)
		if chulsoo[i] == 0:
			chulsoo.pop(i)
		if len(chulsoo) == len(brother):
			answer+=1
	return answer
solution(topping)
