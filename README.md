# 🎮 Quiz App (CLI)

A fun, interactive, emoji-powered command-line quiz game that supports custom question counts, user names, scoring, and automatic result logging.

---

## 📂 Project Files
- **quiz.py** — Main quiz application.
- **questions.json** — Question bank (30 questions included).
- **quiz_results.txt** — Automatically generated to store user results.

---

## 🚀 Features
- Prompts for **user's name**.
- Lets the user choose **how many questions** (up to 30).
- Randomly selects questions from the question bank.
- Fun emojis and clean CLI styling.
- Tracks score and shows performance messages.
- Saves:
  - Name
  - Score
  - Timestamp  
  in `quiz_results.txt`.

---

## 🛠 Requirements
- Python 3.7+
- Uses standard libraries:
  - `json`
  - `random`
  - `time`
  - `datetime`

---

## ▶️ How to Run (PowerShell)

1. Clone the repository  
   ```bash
   git clone https://github.com/Balla-Hemanth-Srinivas/Quiz-app.git
   ```

2. Navigate to the project folder with file **Expense Tracker.py**

3. Run the quiz:
   ```powershell
   python quiz.py
   ```

4. Follow the prompts:
   - Enter your **name**
   - Enter number of questions (1–30)
   - Answer each question as a number (1–4)

---

## 📝 Example Session

```
🎉 Welcome to the Ultimate Quiz Challenge 🎉
👤 Enter your name: Hemanth

How many questions do you want? (max 30)
👉 Enter number: 5

🔹 Question 1: What is the capital of India?
1. Mumbai
2. Delhi
3. Hyderabad
4. Kolkata
👉 Your answer: 2
🎯 Correct! You're a star! 🌟🔥
```

---

## 📄 Result Logging Format
`quiz_results.txt` stores results like:

```
=====================================
Name      : Jayanth
Score     : 4/5
Timestamp : 2025-11-15 22:01:42
=====================================
```

---

## ➕ Future Improvements
- Timer per question  
- Leaderboard system  
- Category-wise quiz  
- GUI version with Tkinter  

---

## 📄 License
Free to use, modify, and improve.
