import random
from question_bank import questions  # Import questions list from external file

def run_quiz():
    score = 0  # Initialize score counter

    # Ask user how many questions they want to attempt
    while True:
        try:
            total_questions = int(input(f"How many questions would you like to attempt? (1-{len(questions)}):\n"))
            if 1 <= total_questions <= len(questions):
                break  # Valid input, exit loop
            else:
                print(f"Please enter a number between 1 and {len(questions)}.")  # Out-of-range check
        except ValueError:
            print('❌ Enter an integer please!')  # Handle non-integer input

    # Randomly select and shuffle questions
    selected_questions = random.sample(questions, total_questions)  # Pick random subset
    random.shuffle(selected_questions)  # Shuffle question order

    # Loop through each question
    for index, question in enumerate(selected_questions):
        print(f"\nQuestion {index + 1}/{total_questions}: {question['prompt']}")  # Show question text

        # Display all options (A, B, C, D)
        for option in question['options']:
            print(option)

        # Get and validate user’s answer
        while True:
            answer = input("Enter your choice ('A','B','C','D' or 'Q' to quit): \n").strip().upper()

            # Ensure input is one of the valid options
            if answer in ['A', 'B', 'C', 'D', 'Q']:
                if answer == 'Q':  # Handle quit option
                    print(f'You have chosen to quit. You scored {score} out of {index} questions attempted.')
                    return  # End quiz early
                break  # Valid answer, exit input loop
            else:
                print("❌ Invalid choice! Please enter A, B, C, D, or Q.")

        # Check answer and update score
        if answer == question['answer']:
            print('Correct! 🎉')
            score += 1
        else:
            print(f"Wrong. Correct answer is: {question['answer']} 🥲")

    # Display final score
    print(f"\n🎯 You scored {score} out of {index + 1} questions. 👍")

# Run quiz when file is executed directly
if __name__ == '__main__':
    run_quiz()
