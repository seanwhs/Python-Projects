import sys
import random
from enum import Enum
import argparse  # For handling command-line arguments


def rps(name='PlayerOne'):
    """Rock-Paper-Scissors game function."""
    # Track total games and wins
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name, player_wins, python_wins, game_count

        # Enum for better readability
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Ask for player input
        player_choice = input(
            f"\n{name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
        )

        # Validate input
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(player_choice)
        computer = int(random.choice("123"))

        # Show choices
        print(f"\n{name}, you chose {RPS(player).name.title()}.")
        print(f"Python chose {RPS(computer).name.title()}.\n")

        # Decide the winner
        def decide_winner(player, computer):
            nonlocal name, player_wins, python_wins
            if (player == 1 and computer == 3) or \
               (player == 2 and computer == 1) or \
               (player == 3 and computer == 2):
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins! ...sorry {name} 🥲"

        # Display result
        print(decide_winner(player, computer))

        # Update and show stats
        game_count += 1
        print(f"\nGame count: {game_count}")
        print(f"{name} wins: {player_wins}")
        print(f"Python wins: {python_wins}")

        # Ask to play again
        while True:
            play_again = input(f"\nPlay again, {name}? (Y to continue, Q to quit): ").lower()
            if play_again in ["y", "q"]:
                break

        # Continue or exit
        if play_again == "y":
            return play_rps()
        else:
            print(f"\n🎉 Thanks for playing, {name}! 👋")
            sys.exit()

    return play_rps


# Run the game
if __name__ == "__main__":
    # Create command-line argument parser
    parser = argparse.ArgumentParser(description='Provide a personalized game experience.')

    # Add a required "name" argument
    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True,
        help='The name of the person playing the game.'
    )

    # Parse arguments
    args = parser.parse_args()

    # Start the game
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
