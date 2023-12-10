# N = int(input())

# def serial(N):
# 	stack = []
# 	for i in range(N):
# 		word = input()
# 		stack.append(word)
# 	stack = {idx:num for idx, num in enumerate(stack)}
# 	count = {}
# 	for k,v in stack.items():
# 		tmp = 0
# 		for j in v:
# 			if  48 <= ord(j) <= 57:
# 				tmp += ord(j)
# 		count[k] = tmp
# 	count = sorted(count.items(), key=lambda x : (x[1]),reverse=True)
# 	result = []
# 	for i,j in count:
# 		result.append(stack[i])
# 	result.sort(key=lambda x : len(x))

# 	for i in result:
# 		print(i)



def sum_num(inputs):
	result = 0
	for i in inputs:
		if i.isdigit():
			result+=int(i)
	return result

N = int(input())
arr = []
for i in range(N):
	a = input()
	arr.append(a)

arr.sort(key = lambda x : (len(x), sum_num(x),x))
for i in arr:
	print(i)
