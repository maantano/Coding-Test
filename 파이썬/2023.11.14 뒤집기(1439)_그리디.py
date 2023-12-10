
import sys
input = sys.stdin.readline

word = input().rstrip()
cnt=0
for i in range(len(word)):
	if word[i] != word[i-1]:
		cnt+=1
print((cnt)//2)

