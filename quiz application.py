# Quiz Application

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Hyderabad", "B. New Delhi", "C. Mumbai", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for AI and Machine Learning?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "3. Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. int", "B. float", "C. bool", "D. string"],
        "answer": "C"
    },
    {
        "question": "5. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    }
]

score = 0

print("===== Welcome to the Python Quiz =====\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct Answer: {q['answer']}\n")

print("===== Quiz Completed =====")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("🎉 Excellent!")
elif percentage >= 60:
    print("👍 Good Job!")
elif percentage >= 40:
    print("🙂 Keep Practicing!")
else:
    print("📚 Study More and Try Again!")