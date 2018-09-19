#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

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
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
#
#
        if move1 != move2:
            if beats(move1, move2):
                print("Player 1 is the winner")
                self.p1score += 1
            else:
                print("Player 2 is the winner")
                self.p2score += 1
        else:
            print("It's a Tie")
#
#

    def play_game(self):
        print("Game start!")
        for round in range(15):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        print(f"Player 1 score: {self.p1score}")
        print(f"Player 2 score: {self.p2score}")


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
