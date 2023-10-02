from questiondata import questions
class Ouestion:
    def __init__(self,qtext,qans):
        self.text=qtext
        self.answer=qans

question_bank=[]
for q in questions:
    question_text=q["question"]
    question_answer=q["correct_answer"]
    new_question=Ouestion(question_text,question_answer)
    question_bank.append(new_question)

class quiz:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list

    def next_question(self):
        current_question=self.question_list[self.question_number]
        user_answer=input(f"Q.{self.question_number+1}:{current_question.text}(True/False):")
        self.question_number+=1
        self.check_answer(user_answer,current_question.answer)

    def still_has_question(self):
        return self.question_number<len(self.question_list)

    def check_answer(self,user_answer,current_answer):
        score=0
        if user_answer.lower()==current_answer.lower:
            score+=1
            print("You got it right.Your current score is "+str(score))
        else:
            print("Your answer is wrong,Correct answer is "+current_answer)
            print("Your current score is " +str(score))

qz=quiz(question_bank)
while qz.still_has_question():
    qz.next_question()

print("Quiz is completed")
