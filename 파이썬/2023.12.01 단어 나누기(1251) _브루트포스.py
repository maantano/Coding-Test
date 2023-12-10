import sys
input = sys.stdin.readline

word = input().rstrip()
answer = []
tmp = []
for i in range(1, len(word) - 1):
	for j in range(i + 1, len(word)):
		a = word[:i][::-1]
		b = word[i:j][::-1]
		c = word[j:][::-1]
		tmp.append(''.join(a+b+c))
for a in tmp:
	answer.append(a)
print(sorted(answer)[0])
