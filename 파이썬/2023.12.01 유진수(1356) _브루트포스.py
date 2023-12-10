import sys
input = sys.stdin.readline

# import string

# tmp = string.digits+string.ascii_lowercase
# print(tmp)
# def convert(num, base) :
# 	q, r = divmod(num, base)
# 	if q == 0 :
# 		return tmp[r]
# 	else :
# 		return convert(q, base) + tmp[r]

# print(convert(10, 2))


n = input().rstrip()
tmp1 = 1
answer = 'NO'
if n == '1':
	print('NO')
	exit()
for i in range(len(n)):
	tmp1*=int(n[i])
	tmp2 = 1
	for j in range(i+1,len(n)):
		tmp2 *= int(n[j])
	if tmp1 == tmp2:
		answer = 'YES'
		break
print(answer)
