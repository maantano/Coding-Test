
n = input()
# n ='a1'
row = n[1]
column = int(ord(n[0]) - ord('a')+1)
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,2),(1,-2)]
result = 0
for step in steps:
	x,y = step
	if not ((int(row) + x) in range(1,9) and (int(column) + y) in range(1,9)):
		continue
	result+=1
print(result)
