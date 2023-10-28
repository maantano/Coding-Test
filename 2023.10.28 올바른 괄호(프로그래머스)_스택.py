# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.


# s=	answer
# s="()()"
# answer = true
# s="(())()"
# answer = true
# s=")()("
# answer = false
s="(()("
# answer = false


def solution(s):
	answer = True
	stack = []
	for i in s:
		if stack:
			if i == "(":
				stack.append(i)
			else:
				stack.pop()
		else:
			if i ==')':
				return False
			else:
				stack.append(i)
	if stack : return False
	else: return True
print(solution(s))



# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def is_pair(s):
	pair = 0
	for x in s:
		if pair < 0: break
		pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
	return pair == 0
