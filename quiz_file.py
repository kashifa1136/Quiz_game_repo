questions = {
    "What is the capital of India? ": "delhi",
    "Which programming language is known as the backbone of web development? ": "javascript",
    "What does CPU stand for? ": "central processing unit",
    "Who is known as the father of Python? ": "guido van rossum",
    "Which planet is known as the Red Planet? ": "mars"
}

score = 0
print("🧠 Welcome to the Quiz Game! 🧠")
print("Answer the following questions:\n")

for question, answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is: {answer}\n")

print(f"Your final score: {score}/{len(questions)}")
