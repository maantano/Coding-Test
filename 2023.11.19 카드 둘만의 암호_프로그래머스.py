# import sys
# input = sys.stdin.readline

# d = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:
# 	 'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
# d2 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
# 	 'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

s = "aukks"
skip = 'wbqd'
index = 5
# answer = ''

# for word in s:
# 	cnt = 0
# 	for i in range(1,index+1):
# 		if d[d2[word]+i] in skip:
# 			cnt+=1
# 	newIdx = (d2[word] + index + cnt) % 26
# 	answer+=d[newIdx]
# print(answer)





import sys
input = sys.stdin.readline



def solution(s,skip,index):
	answer = ''
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	for chk in skip:
		if chk in alpha:
			alpha = alpha.replace(chk,'')

	for i in s:
		change = alpha[(alpha.index(i) + index) % len(alpha)]
		answer+=change
	return answer
