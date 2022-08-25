# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print('Welcome')
score = 0

question = input('First question?\n A: answer1 B: answer2 C: answer3\n')

if question.lower() == 'a':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

question = input('Second question?\n A: answer1 B: answer2 C: answer3\n')

if question.lower() == 'a':
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 2) * 100) + "%")