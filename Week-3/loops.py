# Create a list of dictionaries
quiz = [
    {
        "question": "What is 5 + 5?",
        "options": ["A. 8", "B. 10", "C. 12"],
        "correct_answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun"],
        "correct_answer": "B"
    },
    {
        "question": "What type of data is (1, 2, 3)?",
        "options": ["A. List", "B. Dictionary", "C. Tuple"],
        "correct_answer": "C"
    }
]

score = 0

# Loop through the quiz
for item in quiz:
    print("\n" + item["question"])
    for option in item["options"]:
        print(option)

    answer = input("Enter your answer (A, B, or C): ").upper()

    if answer == item["correct_answer"]:
        print("Correct")
        score += 1
    else:
        print("Wrong")

# Function to calculate result
def result(score, total):
    percentage = (score / total) * 100
    print("\nFinal Score:", score, "/", total)
    print("Percentage:", percentage, "%")

    if percentage >= 50:
        print("PASS")
    else:
        print("FAIL")

result(score, len(quiz))

