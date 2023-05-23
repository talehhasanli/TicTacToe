import pygame

# Initialize pygame
pygame.init()

# Set up the game window
window_width, window_height = 300, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tic Tac Toe')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define game variables
board = [['', '', ''], ['', '', ''], ['', '', '']]
player_turn = 'X'
game_over = False
winner = None

# Define text font
font = pygame.font.Font(None, 80)

# Define winning combinations
winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],  # Row 1
    [(1, 0), (1, 1), (1, 2)],  # Row 2
    [(2, 0), (2, 1), (2, 2)],  # Row 3
    [(0, 0), (1, 0), (2, 0)],  # Column 1
    [(0, 1), (1, 1), (2, 1)],  # Column 2
    [(0, 2), (1, 2), (2, 2)],  # Column 3
    [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
    [(0, 2), (1, 1), (2, 0)]   # Diagonal 2
]

# Define restart button variables
restart_button_width = 100
restart_button_height = 50
restart_button_x = window_width // 2 - restart_button_width // 2
restart_button_y = window_height // 2 - restart_button_height // 2

def draw_board():
    window.fill(BLACK)
    pygame.draw.line(window, WHITE, (window_width // 3, 0), (window_width // 3, window_height), 5)
    pygame.draw.line(window, WHITE, (2 * window_width // 3, 0), (2 * window_width // 3, window_height), 5)
    pygame.draw.line(window, WHITE, (0, window_height // 3), (window_width, window_height // 3), 5)
    pygame.draw.line(window, WHITE, (0, 2 * window_height // 3), (window_width, 2 * window_height // 3), 5)

    for row in range(3):
        for col in range(3):
            center_x = col * window_width // 3 + window_width // 6
            center_y = row * window_height // 3 + window_height // 6
            if board[row][col] == 'X':
                text = font.render('X', True, WHITE)
                window.blit(text, text.get_rect(center=(center_x, center_y)))
            elif board[row][col] == 'O':
                text = font.render('O', True, WHITE)
                window.blit(text, text.get_rect(center=(center_x, center_y)))
# ...

def draw_board():
    window.fill(BLACK)
    pygame.draw.line(window, WHITE, (window_width // 3, 0), (window_width // 3, window_height), 5)
    pygame.draw.line(window, WHITE, (2 * window_width // 3, 0), (2 * window_width // 3, window_height), 5)
    pygame.draw.line(window, WHITE, (0, window_height // 3), (window_width, window_height // 3), 5)
    pygame.draw.line(window, WHITE, (0, 2 * window_height // 3), (window_width, 2 * window_height // 3), 5)
    
    for row in range(3):
        for col in range(3):
            center_x = col * window_width // 3 + window_width // 6
            center_y = row * window_height // 3 + window_height // 6
            if board[row][col] == 'X':
                text = font.render('X', True, WHITE)
                text_rect = text.get_rect(center=(center_x, center_y))
                window.blit(text, text_rect)
            elif board[row][col] == 'O':
                text = font.render('O', True, WHITE)
                text_rect = text.get_rect(center=(center_x, center_y))
                window.blit(text, text_rect)    

        

    pygame.display.update()

# ...




def restart_game():
    global board, player_turn, game_over, winner
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    player_turn = 'X'
    game_over = False
    winner = None

def check_winner():
    global game_over, winner

    for combination in winning_combinations:
        symbols = [board[row][col] for (row, col) in combination]
        if symbols == ['X', 'X', 'X']:
            winner = 'X'
            game_over = True
        elif symbols == ['O', 'O', 'O']:
            winner = 'O'
            game_over = True

    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        # All cells are filled and no winner
        game_over = True

    if game_over:
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a tie!")


def handle_click(row, col):
    global player_turn

    if not game_over and board[row][col] == '':
        board[row][col] = player_turn
        draw_board()
        check_winner()
        player_turn = 'O' if player_turn == 'X' else 'X'

        if game_over:
            pygame.time.wait(1000)  # Wait for 1 second before restarting
            restart_game()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            col = x // (window_width // 3)
            row = y // (window_height // 3)
            handle_click(row, col)
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                restart_game()

    draw_board()

# Quit pygame
pygame.quit()

