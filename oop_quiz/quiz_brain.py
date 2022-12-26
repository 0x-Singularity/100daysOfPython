class QuizBrain:
    def __init__(self,questions_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = questions_list
        
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
        
        
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text} True/False: ")
        self.check_answer(user_answer,current_question.answer)
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        
    def final_score(self):
        return f"{self.score}/{self.question_number}" 
        
    def check_answer(self, user_answer,current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer is {current_answer}")
    