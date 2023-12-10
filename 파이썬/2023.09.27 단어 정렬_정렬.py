# n = int(input())


# arr = []
# def ordCnt(input):
# 	result = 0
# 	for i in range(len(input)):
# 		result += ord(input[i])
# 	return result



# for i in range(n):
# 	arr.append(input())


# arr = sorted(set(arr),key=lambda x : (len(x),ordCnt(x),x))

# for j in arr:
# 	print(j)


n = int(input())

words = [str(input()) for i in range(n)]

words = list(set(words))
words.sort()
words.sort(key=lambda x : len(x))
for i in words:
    print(i)
