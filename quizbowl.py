import sqlite3

connection = sqlite3.connect('databaseConn.py')
cursor = connection.cursor()
questions = cursor.execute("SELECT * FROM QuestAns;").fetchall()  
total_questions = len(questions)
correct_answers = 0
questions_answered = 0  

for question in questions:
    correct_answer = question[2]  # Retrieve the correct answer
    print(f"{question[0]}. {question[1]}")
    user_input = input("Your answer: ")
    if user_input.lower() == correct_answer.lower():
        print("Nice Job! Correct.")
        correct_answers += 1  # adds correct_answers for each correct response
    else:
        print(f"That was not the correct answer. The correct answer is {correct_answer}")
    questions_answered += 1  # adds questions answered
    if questions_answered >= total_questions:  # Check if all questions have been answered
        break

print(f"You have officially reached the end of the quiz. You got {correct_answers} correct out of {total_questions}.")

connection.close()

