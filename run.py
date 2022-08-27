# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from data import Question

print('Welcome')


questiondisplay = [
    "First question?\n (a): answer1 (b): answer2 (c): answer3\n",
    "Second question?\n (a): answer1 (b): answer2 (c): answer3\n",
    "Third question?\n (a): answer1 (b): answer2 (c): answer3\n"
]

questions = [
    Question(questiondisplay[0], "a"),
    Question(questiondisplay[1], "b"),
    Question(questiondisplay[2], "c")
]

def run_game(questions):
    score = 0
    for question in questions:
        useranswer = input(question.prompt)
        if useranswer == question.answer:
            score += 1

    print("You got " + str(score) + " questions correct")
    print("You got " + str((score / 2) * 100) + "%")

run_game(questions)