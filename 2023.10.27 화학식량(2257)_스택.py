# O = 16
# H = 1
# C = 12

import sys
input = sys.stdin.readline

s = input().rstrip()

stack = []
tmp = []
for i in s:
	if i == '(':
