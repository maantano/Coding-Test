
N = int(input())
cnt = N

for i in range(N):
	word = input()
	for j in range(0, len(word)-1):
		if word[j] == word[j+1]:
			pass
		elif word[j] in word[j+1:]:
			cnt -= 1
			break
print(cnt)



n = int(input())
group_word = 0
for _ in range(n):
	word = input()
	error = 0
	for index in range(len(word)-1):
		if word[index] != word[index+1]:
			new_word = word[index+1:]
			if new_word.count(word[index]) > 0:
				error += 1
	if error == 0:
		group_word += 1
print(group_word)
