from quiz import Question
from questiondata import questions
from quiz import Quiz
from ui import QuizInterface

question_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = Quiz(question_bank)
quiz_ui = QuizInterface(quiz)