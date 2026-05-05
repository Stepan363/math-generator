import random

multi_questions = 10 #enter how much multiplication questions you want to answer.
answers = []


def multiplication_question_algorithm():
    for nobody_needs_to_know in range(10):
        int1 = random.randint(1, 50)
        int2 = random.randint(1, 50)
        print(int1, "*", int2, "= ?")
        answers.append(int1 * int2)



multiplication_question_algorithm()
random.shuffle(answers)

print("Answers: ------------------------------")
for i in range(len(answers)):
    print(answers[i])