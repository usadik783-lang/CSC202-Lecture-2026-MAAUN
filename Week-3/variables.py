# List containing dictionaries
quiz = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Kaduna"],
        "correct_answer": "B"
    },
    {
        "question": "Which language is used for CLI programs?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. Photoshop"],
        "correct_answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"],
        "correct_answer": "B"
    }
]

score = 0

# Loop through questions
for q in quiz:
    print("\n" + q["question"])
    
    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ")

    if answer.upper() == q["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

# Function to calculate percentage
def calculate_percentage(score, total):
    return (score / total) * 100

percentage = calculate_percentage(score, len(quiz))

print("\nFinal Score:", score, "/", len(quiz))
print("Percentage:", percentage, "%")

if percentage >= 50:
    print("Pass")
else:
    print("Fail")# List containing dictionaries
quiz = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Kaduna"],
        "correct_answer": "B"
    },
    {
        "question": "Which language is used for CLI programs?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. Photoshop"],
        "correct_answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"],
        "correct_answer": "B"
    }
]

score = 0

# Loop through questions
for q in quiz:
    print("\n" + q["question"])
    
    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ")

    if answer.upper() == q["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

# Function to calculate percentage
def calculate_percentage(score, total):
    return (score / total) * 100

percentage = calculate_percentage(score, len(quiz))

print("\nFinal Score:", score, "/", len(quiz))
print("Percentage:", percentage, "%")

if percentage >= 50:
    print("Pass")
else:
    print("Fail")
