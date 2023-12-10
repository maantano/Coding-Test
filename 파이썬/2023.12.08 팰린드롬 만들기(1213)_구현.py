import sys
from collections import Counter
input = sys.stdin.readline

word = sys.stdin.readline().rstrip()
check_word = Counter(word)

result = ''
mid = ''
cnt = 0
for k,v in check_word.items():

	if v % 2:
		mid = k
		cnt+=1
		if cnt >=2:
			print("I'm Sorry Hansoo")
			exit()
for k,v in sorted(check_word.items()):
	result += k * (v // 2)
print(result + mid + result[::-1])



