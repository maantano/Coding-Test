import sys
n, m = map(int, sys.stdin.readline().split())


stack = []
cnt = {}

for i in range(n):
	tmp = sys.stdin.readline().rstrip()
	if len(tmp) < m:
		continue
	if not cnt.get(tmp):
		cnt[tmp] = 1
	else:
		cnt[tmp] += 1

wordL = cnt.keys()
wordL = sorted(wordL,key=lambda x : (-cnt[x],-len(x),x))

for i in wordL:
	print(i)




import sys
N, M = map(int, sys.stdin.readline().split())
word_cnt = dict()
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    if not word_cnt.get(word):
        word_cnt[word] = 1
    else:
        word_cnt[word] += 1
word_list = word_cnt.keys()
word_list = sorted(word_list, key=lambda x: (-word_cnt[x], -len(x), x))
for word in word_list:
    print(word)


import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

dict = {}
for i in range(n):
  item = list(input().strip())
  if len(item) < m:
    continue
  if "".join(item) in dict:
    dict["".join(item)] += 1
  else :
    dict["".join(item)] = 1


item_list = sorted(dict.items(), key = lambda x:(-x[1], -len(x[0]), x[0]))


for i in item_list:
  print(i[0])
