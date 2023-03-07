# Players for rock, paper, scissors game.

from game_symbols import *
import random


class Player:
    """ Player base class. """
    def __init__(self, id):
        self._id = id
        self._history = []


    def choose(self):
        """ Return one of the valid game symbols."""
        pass


    def record_round(self, yours, theirs, winner_id):
        """ Add tuple of round to game history. """
        self._history.append((yours, theirs, winner_id))


class Human(Player):
    """ Human player at a keyboard. """
    CHAR_2_INT = { "r": ROCK, "p": PAPER, "s": SCISSORS }


    def __init__(self, id):
        super().__init__(id)


    def choose(self):
        """ Prompt at keyboard for valid choice. """
        choice = ""
        while choice not in ['r', 'p', 's']:
            choice = input("(r)ock, (p)aper, or (s)cissors? ")
        return self.__class__.CHAR_2_INT[choice]


class RandomChoice(Player):
    """ Computer player that always makes a random decision. """
    def __init__(self, id):
        super().__init__(id)


    def choose(self):
        """ Return a random choice. """
        choice = random.randint(1,3)
        return choice


class PerfectPercentage(Player):
    """ Computer player that plays based off of percentages. """
    BEATEN_BY = {
        ROCK: PAPER,
        PAPER: SCISSORS,
        SCISSORS: ROCK
    }


    def __init__(self, id):
        super().__init__(id)


    def choose(self):
        if len(self._history) == 0:
            choice = random.randint(1,3)
        else:
            idx = random.randint(0, len(self._history) - 1)
            their_choice = self._history[idx][1]
            choice = self.__class__.BEATEN_BY[their_choice]
        return choice
