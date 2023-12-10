import sys
iput = sys.stdin.readline



def unit(total,idx):
	global ans_max,ans_min
	if idx == n-1:
		ans_min = min(ans_min,total)
		ans_max = max(ans_max,total)
		return
	else:
		for i in range(4):
			if unitl[i] !=0:
				unitl[i] -= 1
				if i == 0:
					unit(total+arr[idx+1],idx+1)
				elif i == 1:
					unit(total-arr[idx+1],idx+1)
				elif i == 2:
					unit(total*arr[idx+1],idx+1)
				elif i == 3:
					unit(int(total/arr[idx+1]),idx+1)


n = int(input())
arr = list(map(int,input().split()))
unitl = list(map(int,input().split()))
ans_max = -1000000001
ans_min = 1000000001
unit(arr[0],0)
print(ans_max)
print(ans_min)
