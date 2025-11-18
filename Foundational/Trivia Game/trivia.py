# Plan of Action:
# 1️⃣ List of Questions
# 2️⃣ Store the answers
# 3️⃣ Randomly pick questions
# 4️⃣ Ask users questions
# 5️⃣ Check if users are correct
# 6️⃣ Keep track of their score
# 7️⃣ Tell users their score

import random
from q_a import questions


def trivia_game():
    """Run a simple trivia game using questions imported from q_a.py."""

    total_questions = 5
    score = 0

    # ✅ Make sure we don’t pick more questions than available
    available_questions = list(questions.keys())
    if total_questions > len(available_questions):
        total_questions = len(available_questions)

    # 🎲 Randomly select questions for the round
    selected_questions = random.sample(available_questions, total_questions)

    # 👋 Welcome message
    print("\n🎯 Welcome to the Trivia Game!\n")
    print(f"Answer {total_questions} questions and see how you score!\n")

    # 🔁 Loop through each question
    for index, question in enumerate(selected_questions, start=1):
        print(f"{index}. {question}")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = questions[question].strip().lower()

        # 🟢 Check if user’s answer is correct
        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {questions[question]}\n")

    # 🏁 Show final score
    print("🎉 Game Over!")
    print(f"Your final score: {score}/{total_questions}\n")


# ▶️ Run the game
if __name__ == "__main__":
    trivia_game()
