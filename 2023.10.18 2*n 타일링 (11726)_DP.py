# a = 2*1
# b = 1*2
# d[1] = 1 => a
# d[2] = 2 => [a,a] , [b,b]
# d[3] = 3 => [a,a,b], [b,a,a] ,[b,b,b]
# d[4] = 5 => [a,a,a,a] [a,a,b,b],[b,b,a,a],[b,a,a,b],[b,b,b,b]
# d[5] = 8 => [a,a,a,a,b],[a,a,b,a,a],[b,a,a,a,a],[b,b,a,a,b],[b,a,a,b,b],[a,a,b,b,b],[b,b,b,a,a],[b,b,b,b,b]

import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 1001

d[0] = 0
d[1] = 1
d[2] = 2

for i in range(3,1001):
	d[i] = (d[i-1]+d[i-2]) % 10007

print(d[n])



