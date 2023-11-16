
chkList = {
'c=' : 0,
'c-' : 0,
'dz=' : 0,
'd-' : 0,
'lj' : 0,
'nj' : 0,
's=' : 0,
'z=': 0,
}


import sys
input = sys.stdin.readline
word = input().rstrip()
answer = 0
for k,v in chkList.items():
	answer += word.count(k)

print(len(word) - answer)



# from collections import deque
# word = deque(list(input().rstrip()))
# # word = list(input().rstrip())
# answer = 0

# while word:
# 	w1 = word.popleft()

# 	w2 = word.popleft()

# 	if w1+w2 in chkList:
# 		answer+=1
# 	else:
# 		answer+=1
# 		word.appendleft(w2)
# print(answer)
