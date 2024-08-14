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

# print(question_bank[0].text) # show list of the question objects (as "object at 0x10f7f2f40")

quiz = QuizBrain(question_bank) # quiz: object | question_bank is the self.question_list = q_list

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
