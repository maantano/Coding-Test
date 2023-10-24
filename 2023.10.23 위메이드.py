# def solution(reqs):
# 	answer = []
# 	actionL = []
# 	idL = []
# 	depositL = []
# 	for i in reqs:
# 		a,b,c = i.split(' ')
# 		actionL.append(a)
# 		idL.append(b)
# 		depositL.append(c)

# 	id_d = list(zip(idL,depositL))
# 	# print(id_d)
# 	for i in range(len(actionL)):
# 		if actionL[i] == 'CREATE':

# def solution(reqs):
# 	answer = []
# 	iL = []
# 	dL = []
# 	for i in reqs:
# 		a,i,d = i.split(' ')
# 		if a == 'CREATE':
# 			if i not in iL:
# 				iL.append(i)
# 				dL.append(-int(d))
# 				answer.append(200)
# 			else:
# 				answer.append(403)
# 				continue
# 		if a == 'DEPOSIT':
# 			if i not in iL:
# 				answer.append(404)
# 				continue
# 			else:
# 				idx = iL.index(i)
# 				dL[idx] -= int(d)
# 				answer.append(200)
# 		if a == 'WITHDRAW':
# 			idx = iL.index(i)
# 			if abs(dL[idx]) < int(d):
# 				answer.append(403)
# 			else:
# 				dL[idx] += int(d)
# 				answer.append(200)
# 				continue
# 	return answer

def solution(reqs):
	answer = []
	iL = []
	dL = []
	for i in reqs:
		a,i,d = i.split(' ')
		if a == 'CREATE':
			if i in iL:
				answer.append(403)
				continue
			else:
				iL.append(i)
				dL.append(-int(d))
				answer.append(200)

		if a == 'DEPOSIT':
			if i in iL:
				idx = iL.index(i)
				dL[idx] -= int(d)
				answer.append(200)
			else:
				answer.append(404)
				continue

		if a == 'WITHDRAW':
			idx = iL.index(i)
			if abs(dL[idx]) < int(d):
				answer.append(403)
			else:
				dL[idx] += int(d)
				answer.append(200)
				continue
	return answer











reqs = ['DEPOSIT 3a 10000','CREATE 3a 300000','WITHDRAW 3a 150000', 'WITHDRAW 3a 150001']
solution(reqs)




