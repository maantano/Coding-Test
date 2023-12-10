# import sys
# input = sys.stdin.readline
# S=input()
# for i in range(len(S)):
# 	if S[i:]==S[i:][::-1]:
# 		print(len(S)+i)
# 		break

# import sys
# input = sys.stdin.readline
string = input()
reversed_string = string[::-1]

length = len(string)
for i in range(length):
	if string[i:] == reversed_string[:length - i]:
		print(length + i)
		break
# abdfhdyrbdbsdfghjkllkjhgfds

# # while True:
# # b = 'abab'
# b = 'abdfhdyrbdbsdfghjkllkjhgfds'
# # b = 'qwerty'
# # b= 'abacaba'
# # b = 'qwerty'
# # print(7//2)
# # print(4//2)
# # print(6//2)

# mid = len(b)//2
# # cnt = 0

# # for i in range(len(b)):
# # len(b[mid:]-1) + len(b[:mid])
# # len(b[mid:]) + len(b[:mid])
# # print('b[mid:] ===>',b[mid:])
# # print('b[:mid] ===>',b[:mid])
# front= b[:mid+1]
# back = b[mid+1:]
# print(front)
# print(back)

# if b[mid+1:] == b[:mid]:
# 	print('1')
# 	print(len(b[mid:]) + len(b[:mid]))
# elif b[mid:] == b[:mid]:
# 	print('2')
# 	print(len(b[mid:]) + len(b[:mid]) + 1)
# else:
# 	print('3')
# 	print(len(b[mid+1:])-1 + len(b[mid+1:])+ len(b[:mid+1])*2)
