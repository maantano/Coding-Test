import sys
input = sys.stdin.readline


# cards1 = ["i", "drink", "water"]
# cards2 = ["want", "to"]
# goal = ["i", "want", "to", "drink", "water"]
cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

['water', 'drink', 'to', 'want', 'i']
['water', 'drink', 'i']
['to', 'want']

def solution(cards1,cards2,goal):
	tmpGoal = goal[::-1]
	cards1 = cards1[::-1]
	cards2 = cards2[::-1]
	answer = []
	while tmpGoal:
		target= tmpGoal.pop()
		if cards1 and cards2:
			if target == cards1[-1]:
				answer.append(cards1.pop())
				answer.append(cards2.pop())
				tmpGoal.pop()
			elif target == cards2[-1]:
				answer.append(cards2.pop())
				answer.append(cards1.pop())
				tmpGoal.pop()
		else:
			if cards1:
				answer.append(cards1.pop())
			else:
				answer.append(cards2.pop())
	if ' '.join(answer).lstrip() == ' '.join(goal).lstrip():
		return 'Yes'
	else:
		return 'No'


print(solution(cards1,cards2,goal))



def solution(cards1, cards2, goal):
	answer = []
	n = len(cards1)
	m = len(cards2)
	i = j = 0
	for word in goal:
		if i < n and word == cards1[i]:
			answer.append(cards1[i])
			i += 1
		if j < m and word == cards2[j]:
			answer.append(cards2[j])
			j += 1
	return 'Yes' if answer == goal else 'No'


def solution(cards1, cards2, goal):
	for i in goal:
		if cards1 and i == cards1[0]:
			cards1.pop(0)
		elif cards2 and i == cards2[0]:
			cards2.pop(0)
		else:
			return 'No'
	return 'Yes'
