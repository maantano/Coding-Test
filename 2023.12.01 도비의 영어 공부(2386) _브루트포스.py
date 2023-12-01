import sys
import string
input = sys.stdin.readline

while True:
	word = input().rstrip().split(' ')
	chk = word[0]
	if chk == '#':
		break
	print(chk,len(''.join(word[1:]).lower().split(chk))-1,sep=' ')


