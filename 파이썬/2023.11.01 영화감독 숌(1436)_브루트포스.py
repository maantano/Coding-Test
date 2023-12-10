n = int(input())
chk = 666
cnt = 0
while True:
	if '666' in str(chk):
		cnt+=1
	if n == cnt:
		print(chk)
		break
	chk +=1
