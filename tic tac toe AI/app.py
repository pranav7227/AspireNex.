from flask import Flask, render_template, request, jsonify
import random
import math

app = Flask(__name__)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def get_empty_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif not get_empty_positions(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (r, c) in get_empty_positions(board):
            board[r][c] = 'X'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[r][c] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for (r, c) in get_empty_positions(board):
            board[r][c] = 'O'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[r][c] = ' '
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

def best_move(board, use_alpha_beta=False):
    best_score = -math.inf
    move = None
    for (r, c) in get_empty_positions(board):
        board[r][c] = 'X'
        if use_alpha_beta:
            score = minimax(board, 0, False, -math.inf, math.inf)
        else:
            score = minimax(board, 0, False, None, None)
        board[r][c] = ' '
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

def random_move(board):
    empty_positions = get_empty_positions(board)
    if empty_positions:
        return random.choice(empty_positions)
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    board = data['board']
    difficulty = data.get('difficulty', 'easy')
    move = None

    if difficulty == 'easy':
        move = random_move(board)
    elif difficulty == 'medium':
        if random.random() < 0.5:
            move = random_move(board)
        else:
            move = best_move(board)
    elif difficulty == 'hard':
        move = best_move(board, use_alpha_beta=True)

    if move:
        board[move[0]][move[1]] = 'X'
    winner = check_winner(board)
    return jsonify(board=board, winner=winner)

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)

