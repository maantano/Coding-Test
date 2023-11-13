time = 100
gold = 200
upgrade = [[0,5],[1500,3],[3000,1]]

# time = 49
# gold = 200
# upgrade = [[0,5],[1500,3],[1501,1]]

# time = 11
# gold = 1000
# upgrade = [[0,5],[100,4],[200,3]]


# max = Math.max(max, Math.floor(time / mineT1) * gold);

# // 1번 업그레이드
# copyT -= Math.ceil(UpCost2 / gold) * mineT1;
# profit = Math.ceil(UpCost2 / gold) * gold - UpCost2;
# max = Math.max(max, Math.floor(copyT / mineT2) * gold + profit);

# // 2번 업그레이드
# copyT = time;
# copyT -= Math.ceil(UpCost2 / gold) * mineT1;
# profit = Math.ceil(UpCost2 / gold) * gold - UpCost2;
#   if (profit >= UpCost3) {
#     profit -= UpCost3;
#     profit += Math.floor(copyT / mineT3) * gold;
#     max = Math.max(max, profit);
#   }
#   //
#   else {
#     copyT -= Math.ceil((UpCost3 - profit) / gold) * mineT2;
#     profit += Math.ceil((UpCost3 - profit) / gold) * gold;
#     profit -= UpCost3;
#     profit += Math.floor(copyT / mineT3) * gold;
#     max = Math.max(max, profit);
#   }

#   return max;
# }
import math
def solution(time,gold,upgrade):
	answer = [time // upgrade[0][1] * gold]
	maxChk = time // upgrade[0][1] * gold
	arr = [gold* time // upgrade[0][1]]
	idx = 1
	while time > 0:
		upgradeTime = math.ceil(upgrade[idx][0] / gold)
		time -= math.floor((upgradeTime * upgrade[idx-1][1]))
		idxWork = upgradeTime * gold
		remain = abs(upgrade[idx][0] - idxWork)
		if time > 0:
			print('remain ====>',remain)
			print('idxWork ===>',idxWork)
			axChk = max(maxChk,(remain + math.floor(time / upgrade[idx][1]) * gold))
			answer.append(remain + math.floor(time / upgrade[idx][1]) * gold)
		print(remain,math.floor(time / upgrade[idx][1]) * gold)

	print(answer)
		# if time > 0:
		# 	idx+=1

# def solution(time,gold,upgrade):
# 	answer = [time // upgrade[0][1] * gold]
# 	maxChk = time // upgrade[0][1] * gold
# 	arr = [gold* time // upgrade[0][1]]
# 	idx = 1
# 	for i in range(1,len(arr)+1):
# 		upgradeTime = math.ceil(upgrade[idx][0] / gold)
# 		time -= upgradeTime * upgrade[idx-1][1]
# 		idxWork = upgradeTime * gold
# 		remain = abs(upgrade[idx][0] - idxWork)
# 		maxChk = max(maxChk,(remain + math.floor((time) / upgrade[idx][1]) * gold))
# 		answer.append(maxChk)
# 		idx+=1
# 	print(answer)









# 	for i in range(1,len(upgrade)):
# 		# upgradeTime = ((upgrade[i][0] // gold) + 1) * upgrade[i-1][1]
# 		if not upgrade[i][0] % gold:
# 			upgradeTime = upgrade[i][0] // gold
# 		else:
# 			upgradeTime = upgrade[i][0] // gold + 1
# 		print('upgradeTime ===>',upgradeTime)
# 		copyT = upgradeTime * gold  + maxChk ## == > 1600,
# 		print('copyT ==>',copyT)
# 		cost =  abs(copyT- upgrade[i][0]) ## ==> 100,
# 		print('cost ==>',cost)
# 		maxChk += cost
# 		print('------------------------------')
# 		# answer = max(maxChk,answer)
# #   max = Math.max(max, Math.floor(time / mineT1) * gold);
# # #   // 1번 업그레이드
# #   copyT -= Math.ceil(UpCost2 / gold) * mineT1;
# #   profit = Math.ceil(UpCost2 / gold) * gold - UpCost2;

# #   max = Math.max(max, Math.floor(copyT / mineT2) * gold + profit);
# #   copyT = time;
# #   copyT -= Math.ceil(UpCost2 / gold) * mineT1;
# #   profit = Math.ceil(UpCost2 / gold) * gold - UpCost2;

# # #   // 남은 profit으로 바로 업그레이드 가능
# #   if (profit >= UpCost3) {
# #     profit -= UpCost3;
# #     profit += Math.floor(copyT / mineT3) * gold;
# #     max = Math.max(max, profit);
# #   }
# #   //
# #   else {
# #     copyT -= Math.ceil((UpCost3 - profit) / gold) * mineT2;
# #     profit += Math.ceil((UpCost3 - profit) / gold) * gold;
# #     profit -= UpCost3;
# #     profit += Math.floor(copyT / mineT3) * gold;
# #     max = Math.max(max, profit);
# #   }
# 	# print(answer)

# 		# maxChk = max(maxChk, )
# 				# print(i)

# # copyT -= Math.ceil(UpCost2 / gold) * mineT1;
# # profit = Math.ceil(UpCost2 / gold) * gold - UpCost2;
# # max = Math.max(max, Math.floor(copyT / mineT2) * gold + profit);



solution(time,gold,upgrade)
