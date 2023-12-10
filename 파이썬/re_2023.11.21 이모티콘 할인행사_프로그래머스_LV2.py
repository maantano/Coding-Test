users= [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
result = [1, 5400]

# def convertSale(per,price):
# 	discount = price * per*0.01
# 	price -=discount
# 	return '{:.0f}'.format(price)

def solution(users, emoticons):
	answer = [0, 0]
	data = [10 ,20, 30, 40]
	discount = []

	def dfs(tmp,depth):
		if depth == len(tmp):
			discount.append(tmp[:])
			return
		for d in data:
			tmp[depth] += d
			dfs(tmp,depth+1)
			tmp[depth] -= d
	dfs([0] *len(emoticons),0)

	for disc in discount:
		cnt = 0
		get = 0

		for i in users:
			pay = 0
			for j in range(len(disc)):
				if i[0] <= disc[j]:
					pay += emoticons[j] * (100 - disc[j])/100
				if pay >= i[1]:
					break
			if pay >= i[1]:
				pay = 0
				cnt +=1
			get += pay
		if cnt >= answer[0]:
			if cnt == answer[0]:
				answer[1] = max(answer[1],get)
			else:
				answer[1] = get
			answer[0] = cnt
	return answer


solution(users, emoticons)
# def solution(users, emoticons):
# 	price = {}
# 	for user in users:
# 		limit = user[1]
# 		disc = user[0]

# 		for i in range(disc,41,10):
# 			if i % 10 == 0:
# 				tmpdisc = i // 10 * 0.01
# 			else:
# 				tmpdisc = (i // 10 + 1)  * 0.01
# 			f

# 	discount = [[] for _ in range(len(emoticons))]
# 	for i in range(len(emoticons)):
# 		for j in 10,20,30,40:
# 			discount[i].append((convertSale(j,emoticons[i])))
# 	print(discount)
# 	answer = []
# 	return answer
# 	answer = [0,0]
# 	return answer
# solution(users, emoticons)
# # convertSale(40,5000)
