import pytest
import json
import pygame
import random
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from unittest.mock import patch
from quiz_game import draw_text, get_random_questions, draw_button, is_button_clicked, show_question

@pytest.fixture
def questions_data():
    with open('questions.json', 'r') as file:
        return json.load(file)['questions']

def test_json_file_structure(questions_data):
    assert isinstance(questions_data, list), "questions_data should be a list"
    for question in questions_data:
        assert 'question' in question
        assert 'options' in question
        assert 'correct' in question

def test_question_options(questions_data):
    for question in questions_data:
        assert len(question['options']) == 4, "Each question should have exactly 4 options"

def test_correct_answer_index(questions_data):
    for question in questions_data:
        correct_index = question['correct']
        assert 0 <= correct_index < len(question['options']), "Correct answer index out of range"

def test_draw_text():
    screen = pygame.display.set_mode((1024, 768))
    draw_text(screen, "Test", (50, 50))
    pygame.display.flip()

def test_draw_button():
    screen = pygame.display.set_mode((1024, 768))
    draw_button(screen, "Test", (50, 50), (200, 50), (200, 200, 200))
    pygame.display.flip()

@patch('pygame.mouse.get_pos', return_value=(100, 100))
def test_is_button_clicked(mock_get_pos):
    screen = pygame.display.set_mode((1024, 768))
    draw_button(screen, "Test", (50, 50), (200, 50), (200, 200, 200))
    pygame.display.flip()

    pygame.event.clear()
    pygame.event.post(pygame.event.Event(MOUSEBUTTONDOWN, {'pos': (100, 100), 'button': 1}))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            assert is_button_clicked(event, (50, 50), (200, 50)) == True

def test_get_random_questions(questions_data):
    random_questions = get_random_questions()
    assert len(random_questions) == 10, "Should return 10 random questions"
    for question in random_questions:
        assert question in questions_data, "Question should be in the original questions data"

def test_show_question():
    screen = pygame.display.set_mode((1024, 768))
    sample_question = {
        'question': "What is the primary structure of a protein?",
        'options': ["A sequence of amino acids", "A folded 3D shape", "A combination of multiple polypeptide chains", "An alpha helix"],
        'correct': 0
    }
    show_question(screen, sample_question, 1, 15)
    pygame.display.flip()
