# Game for player rock, paper, scissors, between two players.


from game_symbols import *
import players


# Mappings of game symbols.
INT_2_WORD = { ROCK: "rock", PAPER: "paper", SCISSORS: "scissors"}


# All possible game outcomes and associated message for player.
OUTCOMES = {
    (ROCK, ROCK): (0, "Draw!"),
    (PAPER, PAPER): (0, "Draw!"),
    (SCISSORS, SCISSORS): (0, "Draw!"),
    (ROCK, SCISSORS): (1, "Rock blunts scissors. You win!"),
    (PAPER, ROCK): (1, "Paper wraps rock. You win!"),
    (SCISSORS, PAPER): (1, "Scissors cut paper. You win!"),
    (ROCK, PAPER): (2, "Paper wraps rock. You lose!"),
    (PAPER, SCISSORS): (2, "Scissors cut paper. You lose!"),
    (SCISSORS, ROCK): (2, "Rock blunts scissors. You lose!")
}


def main(p1, p2):
    """ Plays a game of rock, paper, scissors between two players. Assumes that
    the players have ids of 1 and 2 respectively. """
    play_again = "y"
    while play_again == "y":
        p1_choice = p1.choose()
        p2_choice = p2.choose()
        print(INT_2_WORD[p1_choice], end=" vs ")
        print(INT_2_WORD[p2_choice])
        (winner_id, outcome_descr) = OUTCOMES[(p1_choice, p2_choice)]
        print(outcome_descr)
        p1.record_round(p1_choice, p2_choice, winner_id)
        p2.record_round(p2_choice, p1_choice, winner_id)
        play_again = input("Play again? [y/n] ")


if __name__ == "__main__":
    p1 = players.Human(1)
    # p2 = players.RandomChoice(2)
    p2 = players.PerfectPercentage(2)
    main(p1, p2)
