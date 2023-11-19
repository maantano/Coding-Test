import sys
input = sys.stdin.readline


cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

# # total = list(zip(deliveries,pickups))
# # total[0][0] = 200
# # print(total[0][0])
# # print(total[0])
# # print(sum(total))
# # print(total.pop())
# # print(total)
# # while total:
# answer =  0
# while sum(deliveries) != 0 and sum(pickups) != 0:
# 	dTmp= 0
# 	pTmp = 0
# 	maxD  = 0
# 	for i in range(n-1,-1,-1):
# 		print(deliveries[i])
# 		print(pickups[i])
# 		print(deliveries)
# 		print(pickups)
# 		print('------------------------')
# 		if pTmp+pickups[i] < cap:
# 			# dTmp += deliveries[i]
# 			deliveries[i] = 0
# 			pTmp += pickups[i]
# 			pickups[i] = 0
# 			maxD = max(maxD,i+1)
# 			print('maxD ===>',maxD)
# 		else:
# 			answer += maxD *2
# 			print('answer ===>',answer)
# 			deliveries[i] = 0
# 			pickups[i] = 0
# 			n = i+1
# 			break
# print(answer)

		# dTmp =+ deliveries[i]
		# deliveries[i] = 0
		# maxD = max(i,maxD) + 1

		# if pTmp > cap:
		# 	break
		# else:
		# 	pTmp =+pickups[i]
		# 	pickups[i] = 0






def solution(cap, n, deliveries, pickups):
	deliveries = deliveries[::-1]
	pickups = pickups[::-1]
	answer = 0

	have_to_deli = 0
	have_to_pick = 0

	for i in range(n):
		have_to_deli += deliveries[i]
		have_to_pick += pickups[i]

		while have_to_deli > 0 or have_to_pick > 0:
			have_to_deli -= cap
			have_to_pick -= cap
			answer += (n - i) * 2

	return answer


solution(cap, n, deliveries, pickups)
