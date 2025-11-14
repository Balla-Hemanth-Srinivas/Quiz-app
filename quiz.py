import json
import random
import time
from datetime import datetime

RESULTS_FILE = "quiz_results.txt"

# =========================== HEADER ===========================

def show_header():
    print("\n" + "=" * 50)
    print("🎉 Welcome to the Ultimate Quiz Challenge 🎉")
    print("=" * 50)
    print("Fun questions, emojis, and challenges await! 🤩🔥\n")
    time.sleep(1)

# =========================== LOAD QUESTIONS ===================

def load_questions():
    try:
        with open("questions.json") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("❌ Error: questions.json not found!")
        return []
    except json.decoder.JSONDecodeError:
        print("❌ Error: JSON formatting issue!")
        return []

# =========================== USERNAME PROMPT ==================

def get_username():
    while True:
        name = input("👤 Enter your name: ").strip()
        if name:
            return name
        print("⚠️ Name cannot be empty!")

# =========================== HOW MANY QUESTIONS ===============

def ask_how_many(total):
    while True:
        try:
            print(f"\nHow many questions do you want? (max {total})")
            count = int(input("👉 Enter number: "))
            if 1 <= count <= total:
                return count
            print(f"⚠️ Pick a number between 1 and {total}!")
        except ValueError:
            print("⚠️ Please enter a valid number!")

# =========================== ASK ONE QUESTION =================

def ask_question(q, index):
    print(f"\n🔹 Question {index + 1}: {q['question']}")
    for i, opt in enumerate(q["options"], 1):
        print(f"   {i}. {opt}")

    while True:
        try:
            ans = int(input("👉 Your answer: "))
            if 1 <= ans <= len(q["options"]):
                return ans
            print("⚠️ Invalid option number!")
        except ValueError:
            print("⚠️ Please type a number!")

# =========================== FEEDBACK =========================

def feedback(is_correct):
    if is_correct:
        print("🎯 Correct! You're a star! 🌟🔥")
    else:
        print("❌ Wrong! Don't worry, keep going! 💪😊")

# =========================== FINAL SCORE ======================

def show_final(name, score, total):
    print("\n" + "=" * 40)
    print("📊 Quiz Completed!")
    print(f"👤 Player: {name}")
    print(f"🏆 Score : {score}/{total}")

    if score == total:
        print("🥇 PERFECT! You're unstoppable! 🤯🔥")
    elif score >= total * 0.7:
        print("👏 Great work! You're sharp! 😄")
    elif score >= total * 0.4:
        print("🙂 Decent attempt! Keep learning!")
    else:
        print("😅 You need more practice. You got this!")
    print("=" * 40 + "\n")

# =========================== SAVE RESULTS =====================

def save_results(name, score, total):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(RESULTS_FILE, "a") as f:
        f.write("=====================================\n")
        f.write(f"Name      : {name}\n")
        f.write(f"Score     : {score}/{total}\n")
        f.write(f"Timestamp : {timestamp}\n")
        f.write("=====================================\n\n")

    print("📁 Your results have been saved to quiz_results.txt")

# =========================== MAIN LOGIC =======================

def main():
    show_header()

    name = get_username()
    questions = load_questions()

    if not questions:
        return

    total_available = len(questions)
    count = ask_how_many(total_available)

    chosen_questions = random.sample(questions, count)
    score = 0

    for index, q in enumerate(chosen_questions):
        ans = ask_question(q, index)
        correct = ans == q["answer"]

        if correct:
            score += 1

        feedback(correct)
        time.sleep(0.5)

    show_final(name, score, count)
    save_results(name, score, count)

if __name__ == "__main__":
    main()
