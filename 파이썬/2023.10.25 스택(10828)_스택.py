import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
	tmp = input().split()
	if tmp[0] == 'push':
		arr.append(tmp[1])
	elif tmp[0] == 'top':
		if arr:
			print(arr[-1])
		else:
			print(-1)
	elif tmp[0] == 'pop':
		if arr:
			print(arr.pop())
		else:
			print(-1)
	elif tmp[0] == 'size':
		print(len(arr))
	elif tmp =='empty':
		if arr:
			print(1)
		else:
			print(0)


import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
