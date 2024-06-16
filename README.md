# Protein Quiz Game

This project is a quiz game about proteins, developed as part of the Python programming course at the Weizmann Institute of Science.
The game is designed to test and improve knowledge about proteins through an interactive and fun interface.

## Scientific Background

Proteins are essential biomolecules that play critical roles in almost all biological processes.
They are composed of amino acids and have various structures and functions.
Understanding proteins is fundamental to the fields of biology, biochemistry, and medicine.

### Key Concepts

1. **Primary Structure**: The sequence of amino acids in a protein.
2. **Secondary Structure**: Includes alpha helices and beta sheets formed by hydrogen bonds between the backbone atoms.
3. **Tertiary Structure**: The three-dimensional folded shape of a single polypeptide chain.
4. **Quaternary Structure**: The arrangement of multiple polypeptide chains into a single functional unit.
5. **Enzymes**: Proteins that act as catalysts to speed up chemical reactions.
6. **Hemoglobin**: A protein in red blood cells responsible for transporting oxygen.
7. **Denaturation**: The loss of a protein's native structure and function due to external stressors.

For more detailed information on proteins, please refer to the following resources:
- [Protein Structure and Function](https://en.wikipedia.org/wiki/Protein_structure)
- [Amino Acids](https://en.wikipedia.org/wiki/Amino_acid)
- [Enzymes](https://en.wikipedia.org/wiki/Enzyme)

## Technical Details

### Prerequisites

- Python 3.10 or higher
- Pygame

To install the required dependencies, run:
```
pip install -r requirements.txt
```

### requirements.txt

```
pygame
pytest
```

### Running the Game

To start the quiz game, run:
```
python quiz_game.py
```

### How to Play

1. **Start the Game**: Click the "Start" button on the welcome screen to begin the quiz.
2. **Answer Questions**: For each question, you have 15 seconds to select the correct answer from four options. If you answer incorrectly, you will receive an additional 10 seconds to try again.
3. **Score**: You earn 10 points for each correct answer, whether answered correctly on the first or second attempt.
4. **End of Game**: After answering 10 questions, your total score will be displayed.

### Input and Data Files

The game uses a JSON file (`questions.json`) to store the quiz questions and answers. The format of the file is as follows:
```
{
  "questions": [
    {
      "question": "What is the primary structure of a protein?",
      "options": ["A sequence of amino acids", "A folded 3D shape", "A combination of multiple polypeptide chains", "An alpha helix"],
      "correct": 0
    },
    ...
  ]
}
```
The questions in the JSON file are shuffled to ensure a varied experience each time the game is played.

### Code Structure

The main script `quiz_game.py` contains the following key parts:
- **Initialization**: Sets up the Pygame environment and loads the questions from the JSON file.
- **Helper Functions**: Functions to draw text, buttons, and manage question display.
- **Main Game Loop**: Handles the game flow, user interactions, and timing.

### Testing

To ensure the game works correctly, we have included tests using `pytest`. The test file is named `test_quiz_game.py` and includes the following checks:
- JSON file structure
- Each question has exactly 4 options
- The correct answer index is within the options range
- Pygame functions and button interactions
- Game flow logic, such as time management and score updating

To run the tests, simply use:
```
pytest
```

### Example Run

1. Run the game using the command: `python quiz_game.py`.
2. The welcome screen will appear with "Start" and "Quit" buttons.
3. Click "Start" to begin the quiz.
4. Answer the questions by clicking on the options.
5. The game will display your score at the end with an option to quit.

## Course Reference

This project was originally implemented as part of the [Python programming course](https://github.com/szabgab/wis-python-course-2024-04) at the [Weizmann Institute of Science](https://www.weizmann.ac.il/pages/) taught by [Gabor Szabo](https://szabgab.com/).
