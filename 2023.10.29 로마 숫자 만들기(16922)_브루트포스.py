import sys
input = sys.stdin.readline

f = {'I':1, 'V':5, 'X':10, 'L':50}

from itertools import combinations_with_replacement
n = int(input().rstrip())
l = list(combinations_with_replacement(f.values(),n))

answer = []
for i in l:
	answer.append(sum(i))
print(len(set(answer)))


