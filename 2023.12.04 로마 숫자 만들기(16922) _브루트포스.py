import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement
rome = {'I':5,'V':5,'X':10,'L':50}

n = int(input())
combi = list(combinations_with_replacement(rome.values(),n))

answer = []
for i in combi:
	answer.append(sum(i))
print(len(answer))
