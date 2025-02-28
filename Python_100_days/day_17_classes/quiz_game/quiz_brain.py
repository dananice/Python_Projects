# TODO: Asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0   #attribute
        self.score = 0   #attribute
        self.question_list = q_list #attribute

# Method
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


# Retrieve the item at the current question_number from the question_list.
# Use the input() function to show the user the Question text ans ask for the user's answer
# Method
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

# checks if the answer is correct
    # Method
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
