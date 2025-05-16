import sys

# Define a list of tuples where each tuple contains a question, options, and correct answer
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Madrid", "D. London"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Jupiter", "B. Mars", "C. Saturn", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who is the author of 'To Kill a Mockingbird'?",
        "options": ["A. J.K. Rowling", "B. Harper Lee", "C. Charles Dickens", "D. Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue whale", "C. Giraffe", "D. Lion"],
        "answer": "B"
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["A. China", "B. Brazil", "C. Russia", "D. USA"],
        "answer": "B"
    }
]


def display_question(question_data):
    """
    Display a question and its options to the user.
    """
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter your choice (A/B/C/D or Q to quit): ").strip().upper()
    return user_answer


def main():
    total_questions = len(questions)
    current_question = 0
    total_money = 0

    print("Welcome to the Quiz Game!")

    while current_question < total_questions:
        question_data = questions[current_question]
        user_answer = display_question(question_data)

        if user_answer == "Q":
            print("You have chosen to quit the game.")
            break

        if user_answer == question_data["answer"]:
            total_money += 1000  # Increment money for each correct answer
            print("Correct!")
        else:
            print("Incorrect!")
            break

        current_question += 1

    print(f"\nYou won ${total_money}.00!")
    print("Thank you for playing.")


if __name__ == "__main__":
    main()




