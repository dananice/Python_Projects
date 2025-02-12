from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

    ''' 
    originally we used the information in data.py for the questions. once we got the
    game up and running correctly we changed to questions from "OPEN TRIVIA.COM
    you go to opentrivia.com click on API fill out API Helper as you choose
    GENERATE API URL - copy url - paste into new tab - copy information into question_data - reformat code - notice its a  dictionary w\n a dictionary
    remove the enclosing dictionary - { "response_code": 0, "results":} - reformat code - note the difference in key value pair names
    update attributes in main.py to reflect the new names
    question_text = question["text"] becomes question_text = question["question"] 
    question_answer = question["answer"] becomes question_answer = question["correct_answer"]
    '''

quiz = QuizBrain(question_bank)

# to loop the remaining questions
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
