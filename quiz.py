import random
from termcolor import colored, cprint

QUESTION = "question"
OPTION = "option"
ANSWER = "answer"


def ask_question(index, question, options):

    print(f"Question {index}: {question}")

    for option in options:
        print(option)
    return input("Your answer: ").upper().strip()


def run_quiz(quiz):
    random.shuffle(quiz)
    score = 0
    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION], item[OPTION])
        if answer == item[ANSWER]:
            cprint("Correct", "green")
            score += 1
        else:
            cprint(f"Incorrect! The correct answer is {item[ANSWER]}", "red")
    cprint(f"Yor final score is {score} out of {len(quiz)}", "blue")


def main():
    quiz = [
        {
            QUESTION: "What is the capital of France?",
            OPTION: ["A. Berlin", "B. Madrid", "C. Paris", "D. London"],
            ANSWER: "C"
        },
        {
            QUESTION: "Which planet is known as the Red Planet?",
            OPTION: ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            ANSWER: "B"
        },
        {
            QUESTION: "Who wrote 'Romeo and Juliet'?",
            OPTION: ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
            ANSWER: "C"
        },
        {
            QUESTION: "What is the largest mammal on Earth?",
            OPTION: ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"],
            ANSWER: "B"
        },
        {
            QUESTION: "Which element has the chemical symbol 'O'?",
            OPTION: ["A. Oxygen", "B. Gold", "C. Osmium", "D. Zinc"],
            ANSWER: "A"
        }
    ]

    run_quiz(quiz)


if __name__ == "__main__":
    main()
