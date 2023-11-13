# board = ["O.X", ".O.", "..X"]
# board = ["OOO", "...", "XXX"]
board = ["OOO", "...", "XXX"]


def won(board, t):
# 가로줄 판단.

	for row in board:
		if row == [t, t, t]:

			return True

	# 세로줄 판단.
	for col in range(3):
		if [board[row][col] for row in range(3)] == [t, t, t]:
			return True

	# 대각선 판단.
	if [board[0][0], board[1][1], board[2][2]] == [t, t, t]:
		return True

	if [board[2][0], board[1][1], board[0][2]] == [t, t, t]:
		return True

	return False


def solution(board):
	board = [list(row) for row in board]
	xcnt,ocnt = 0,0
	for i in board:
		xcnt += i.count('X')
		ocnt += i.count('O')

	if not (ocnt == xcnt or ocnt == xcnt +1):
		return 0
	if won(board,'O') and won(board,'X'):
		return 0
	if won(board,'O') and ocnt != xcnt +1:
		return 0
	if won(board,'X') and ocnt != xcnt:
		return 0
	return 1
print(solution(board,))
