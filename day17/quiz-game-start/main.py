# Object: Question | Attributes: text, answer
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list()
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)  # new_question = object
    # para passar os atributos da classe Question, são usados question_text e question_answer
    question_bank.append(new_question) # objeto new_question (utilizar .text ou .answer) sendo adicionado à lista question_bank

# print(question_bank[0].text) # show text

quiz = QuizBrain(question_bank) # quiz: object
quiz.next_question()
