#!/usr/bin/env python3
"""
GUI Quiz App Launcher
This file properly initializes the GUI version of the quiz app.
"""

from ui import QuizInterface
from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

def main():
    """Initialize and run the GUI quiz app."""
    
    # Create question bank from API data
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    # Initialize quiz brain
    quiz = QuizBrain(question_bank)
    
    # Start GUI
    quiz_ui = QuizInterface(quiz)

if __name__ == "__main__":
    main()
