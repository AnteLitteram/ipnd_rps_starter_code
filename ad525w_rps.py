#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'scissors'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        if move1[0] == 'q':
            self.p1score = 5
            self.p2score = 5
        if move1 in moves:
            move2 = self.p2.move()
            print(f"Player 1: {move1}  Player 2: {move2}")
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)
#
            if move1 != move2:
                if beats(move1, move2):
                    self.p1score += 1
                    print(f"Player 1 wins and has {self.p1score} total.\n")
                else:
                    self.p2score += 1
                    print(f"Player 2 wins and has {self.p2score} total.\n")
            else:
                print(f"You tied that round.\n")
        else:
            print("Not a valid selection. use q or quit to end the game.\n")

    def play_game(self):
        print("\nThe rules are as follows:")
        print("Rock beats scissors, scissors beats paper, paper beats rock.")
        print("The fist player to reach a score of 5 wins the game.")
        print('Type "q" or "quit" to end game.\n')
        while self.p1score < 5 and self.p2score < 5:
            self.play_round()
        print("Game over!")
        print(f"Player 1 score: {self.p1score}")
        print(f"Player 2 score: {self.p2score}")


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move = input('Please enter "rock", "paper" or "scissors": ')
        return move


class ReflectPlayer(Player):
    def move(self):
        return "paper"


class CyclePlayer(Player):
    def move(self):
        return "rock"

    if __name__ == '__main__':
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
