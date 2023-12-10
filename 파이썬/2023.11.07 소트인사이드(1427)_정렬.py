import sys
input = sys.stdin.readline

n = input().rstrip()
arr = list(map(str,n))
arr.sort(reverse=True)
print(''.join(arr))
