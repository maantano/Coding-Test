# import sys
# d = {i:0 for i in range(1,10)}
# n = input().rstrip()
# for i in n:
# 	d[int(i)] +=1
# maxNum,maxD = sorted(d.items(),key=lambda x : x[1],reverse=True)[0]
# sixNnie = sum(divmod((d[6] + d[9]),2))

# if maxNum == 9 or maxNum == 6:
# 	print(sixNnie)
# else:
# 	print(maxD)




import sys
input = sys.stdin.readline
n = int(input())
card = [0] * 10
for i in str(n):
	if i == "9" or i == "6":
		if card[6] == card[9]:
			card[6] += 1
		else:
			card[9] += 1
	else:
		card[int(i)] += 1

print(max(card))
