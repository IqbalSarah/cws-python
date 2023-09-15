# # Define the list of questions and their corresponding answer choices.
# questions = [
#     {
#         "question": "What is the capital of France?",
#         "choices": ["a) London", "b) Madrid", "c) Paris", "d) Rome"],
#         "correct_answer": "c",
#     },
#     {
#         "question": "Which of the following is a prime number?",
#         "choices": ["a) 15", "b) 23", "c) 21", "d) 27"],
#         "correct_answer": "b",
#     },
#     {
#         "question": "Which planet is known as the 'Red Planet'?",
#         "choices": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
#         "correct_answer": "b",
#     },
#     {
#         "question": "What is the largest mammal on Earth?",
#         "choices": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Dolphin"],
#         "correct_answer": "b",
#     },
#     {
#         "question": "Who wrote the play 'Romeo and Juliet'?",
#         "choices": [
#             "a) William Shakespeare",
#             "b) Jane Austen",
#             "c) Charles Dickens",
#             "d) Mark Twain",
#         ],
#         "correct_answer": "a",
#     },
# ]

# # Initialize the user's score.
# score = 0

# # Iterate through the questions and present them to the user.
# for question_data in questions:
#     print(question_data["question"])
#     for choice in question_data["choices"]:
#         print(choice)

#     # Get the user's answer.
#     user_answer = input("Enter your choice (a, b, c, or d): ").lower()

#     # Check if the user's answer is correct.
#     if user_answer == question_data["correct_answer"]:
#         print("Correct!\n")
#         score += 1
#     else:
#         print("Incorrect!\n")

# # Display the user's final score.
# print(f"Your final score is: {score}/{len(questions)}")

# # Provide feedback based on the user's score.
# if score == len(questions):
#     print("Great job! You got a perfect score!")
# elif score >= len(questions) / 2:
#     print("Good job! You did well.")
# else:
#     print("Keep practicing! You know nothing!")


# Without using dictionary

# Define the list of questions, answer choices, and correct answers.
questions = [
    "What is the capital of France?",
    "Which of the following is a prime number?",
    "Which planet is known as the 'Red Planet'?",
    "What is the largest mammal on Earth?",
    "Who wrote the play 'Romeo and Juliet'?",
]

choices = [
    ["a) London", "b) Madrid", "c) Paris", "d) Rome"],
    ["a) 15", "b) 23", "c) 21", "d) 27"],
    ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
    ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Dolphin"],
    ["a) William Shakespeare", "b) Jane Austen", "c) Charles Dickens", "d) Mark Twain"],
]

correct_answers = ["c", "b", "b", "b", "a"]

score = 0

for i in range(len(questions)):
    print(f"Question {i + 1}:")
    print(questions[i])
    for choice in choices[i]:
        print(choice)

    user_answer = input("Enter your choice (a, b, c, or d): ").lower()

    if user_answer == correct_answers[i]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

print(f"Your final score is: {score}/{len(questions)}")

if score == len(questions):
    print("Great job! You got a perfect score!")
elif score >= len(questions) / 2:
    print("Good job! You did well.")
else:
    print("Keep practicing! You know nothing!")
