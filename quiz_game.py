import pygame
import json
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1024, 768
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FONT = pygame.font.Font(None, 36)
QUESTION_TIME = 15
EXTRA_TIME = 10

# Load questions from JSON
with open('questions.json', 'r') as file:
    questions_data = json.load(file)['questions']

# Helper functions
def draw_text(screen, text, position, color=BLACK):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, position)

def get_random_questions():
    return random.sample(questions_data, 10)

def draw_button(screen, text, position, size, color, border_color=BLACK):
    pygame.draw.rect(screen, color, (*position, *size))
    pygame.draw.rect(screen, border_color, (*position, *size), 2)
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(position[0] + size[0] // 2, position[1] + size[1] // 2))
    screen.blit(text_surface, text_rect)

def is_button_clicked(event, position, size):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if position[0] <= mouse_pos[0] <= position[0] + size[0] and position[1] <= mouse_pos[1] <= position[1] + size[1]:
            return True
    return False

def show_question(screen, question_data, question_number, time_left):
    screen.fill(WHITE)
    draw_text(screen, f"Question {question_number}/10", (50, 20))
    draw_text(screen, question_data['question'], (50, 50))
    button_size = (900, 50)
    button_gap = 20
    for i, option in enumerate(question_data['options']):
        draw_button(screen, f"{i + 1}. {option}", (50, 150 + i * (button_size[1] + button_gap)), button_size, GRAY)
    draw_text(screen, f"Time left: {time_left}", (50, 600))
    draw_button(screen, "Quit", (WIDTH - 250, HEIGHT - 100), (200, 50), RED)
    pygame.display.flip()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Quiz Game About Proteins")

    questions = get_random_questions()
    current_question = 0
    score = 0
    start_time = time.time()
    first_attempt = True
    extra_time_given = False
    game_started = False
    game_over = False

    running = True
    while running:
        if not game_started and not game_over:
            screen.fill(WHITE)
            draw_text(screen, "Welcome to Quiz Game About Proteins!", (WIDTH // 2 - 200, HEIGHT // 2 - 100))
            draw_button(screen, "Start", (WIDTH // 2 - 100, HEIGHT // 2), (200, 50), GREEN)
            draw_button(screen, "Quit", (WIDTH // 2 - 100, HEIGHT // 2 + 70), (200, 50), RED)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif is_button_clicked(event, (WIDTH // 2 - 100, HEIGHT // 2), (200, 50)):
                    game_started = True
                    game_over = False
                    questions = get_random_questions()  # Reset questions for new game
                    current_question = 0
                    score = 0
                    start_time = time.time()
                elif is_button_clicked(event, (WIDTH // 2 - 100, HEIGHT // 2 + 70), (200, 50)):
                    running = False
        elif game_over:
            screen.fill(WHITE)
            draw_text(screen, f"Game Over! Your score: {score}", (WIDTH // 2 - 100, HEIGHT // 2 - 50))
            draw_button(screen, "Quit", (WIDTH // 2 - 100, HEIGHT // 2), (200, 50), RED)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif is_button_clicked(event, (WIDTH // 2 - 100, HEIGHT // 2), (200, 50)):
                    running = False
        else:
            if current_question >= len(questions):
                game_over = True
                game_started = False
                continue

            time_elapsed = time.time() - start_time
            time_left = QUESTION_TIME - int(time_elapsed)
            if time_left < 0:
                if not extra_time_given:
                    time_left = EXTRA_TIME
                    extra_time_given = True
                    first_attempt = False
                else:
                    current_question += 1
                    start_time = time.time()
                    extra_time_given = False
                    first_attempt = True
                    continue

            show_question(screen, questions[current_question], current_question + 1, time_left)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif is_button_clicked(event, (50, 150), (900, 50)):
                    chosen_option = 0
                elif is_button_clicked(event, (50, 220), (900, 50)):
                    chosen_option = 1
                elif is_button_clicked(event, (50, 290), (900, 50)):
                    chosen_option = 2
                elif is_button_clicked(event, (50, 360), (900, 50)):
                    chosen_option = 3
                elif is_button_clicked(event, (WIDTH - 250, HEIGHT - 100), (200, 50)):
                    running = False
                else:
                    continue

                if chosen_option == questions[current_question]['correct']:
                    score += 10
                    if first_attempt:
                        draw_text(screen, "Correct! First attempt.", (50, 550), GREEN)
                    else:
                        draw_text(screen, "Correct! Second attempt.", (50, 550), BLUE)
                    pygame.display.flip()
                    time.sleep(1)
                    current_question += 1
                    start_time = time.time()
                    extra_time_given = False
                    first_attempt = True
                else:
                    if first_attempt:
                        draw_text(screen, "Wrong answer. You have 10 more seconds to try again!", (50, 550), RED)
                        pygame.display.flip()
                        time.sleep(2)
                        start_time = time.time() - QUESTION_TIME + 10
                        first_attempt = False
                    else:
                        draw_text(screen, "Wrong answer. Moving to the next question.", (50, 550), RED)
                        pygame.display.flip()
                        time.sleep(1)
                        current_question += 1
                        start_time = time.time()
                        extra_time_given = False
                        first_attempt = True

    pygame.quit()

if __name__ == "__main__":
    main()
