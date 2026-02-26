
def quiz():
    print("=== Phishing Awareness Quiz ===\n")

    questions = [
        {
            "q": "Which of these is a sign of phishing?",
            "options": ["A) Unknown sender", "B) Urgent request for password", "C) Suspicious links", "D) All of the above"],
            "answer": "D"
        },
        {
            "q": "What should you check before clicking a link?",
            "options": ["A) Hover to see actual URL", "B) Trust sender blindly", "C) Ignore security warnings", "D) None"],
            "answer": "A"
        },
        {
            "q": "Best way to avoid phishing?",
            "options": ["A) Use strong passwords", "B) Enable 2FA", "C) Verify sender identity", "D) All of the above"],
            "answer": "D"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['q']}")
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer: ").strip().upper()
        if ans == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"Your Score: {score}/{len(questions)}")
    print("Stay safe online! 🚀")

if __name__ == "__main__":
    quiz()