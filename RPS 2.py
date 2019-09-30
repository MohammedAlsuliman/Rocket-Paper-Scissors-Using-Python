#!/usr/bin/env python3

from random import randint


class Player:

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):

    def move(self):
        return input("Rock or Paper or Scissors ??").lower()


class RandomPlayer(Player):

    def move(self, number):
        s = ["rock", "paper", "scissors"]
        computer = s[randint(0, 2)]
        return computer


class CyclePlayer(Player):

    def move(self, number):
        s = ["rock", "paper", "scissors"]
        return s[number]


class RockPlayer(Player):
    def move(self, number):
        return 'rock'


def beats(one, two):
    if ((one == 'rock' and two == 'scissors') or
       (one == 'scissors' and two == 'paper') or
       (one == 'paper' and two == 'rock')):

        return True


class ReflectPlayer(Player):

    # The first round the computer will play a random play and then he will be
    # learnd to play the last move of a hhuman player
    def learn(self, my_move, their_move):
        mm = my_move
        return mm

    def move(self, number):
        pass


# =======================================================================================================================================
class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self, number, rounds, if_ref, comp_move):
        move1 = self.p1.move()
        if if_ref and rounds == 1:
            s = ["rock", "paper", "scissors"]
            move2 = s[randint(0, 2)]
        elif (if_ref) and ((comp_move == "rock") or
                           (comp_move == "paper") or
                           (comp_move == "scissors")):

            move2 = comp_move
        else:
            move2 = self.p2.move(number)
        User_wins = 0
        Computer_wins = 0
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("You Won The Round!")
            User_wins = User_wins + 1
        elif (move1 == move2):
            print("Its a Draw")
            return False
            # i return false because if you see line 117 i put if the condion
            # is false run the loop again because its a draw
            # i couldnt see another way to solve this
        elif beats(move2, move1):
            print("You Lost The Round!")
            Computer_wins = Computer_wins + 1
        else:
            print("Bad input Please try again..")
            return False
        mmo = move1
        self.p1.learn(move1, move2)
        return [User_wins, Computer_wins, mmo]

    def play_game(self, if_ref):
        User_wins = 0
        Computer_wins = 0
        Counter_Loop = 1
        Cycle_Strategy = 0
        lsit = [0, 0, 0]
        com_move = 0
        mmo = lsit[2]
        rounds = int(input("How many Rounds do you want to play ??"))+1
        print("Game start!")
        while True:
            print(f"Round {Counter_Loop}:")
            if Cycle_Strategy > 2:
                Cycle_Strategy = 0
            lsit = self.play_round(Cycle_Strategy, Counter_Loop, if_ref, mmo)
            Cycle_Strategy = Cycle_Strategy + 1
            if not lsit:
                continue
            User_wins = User_wins + lsit[0]
            Computer_wins = Computer_wins + lsit[1]
            print(f"Your Score : ", User_wins)
            print(f"Computer Score : ", Computer_wins)
            mmo = lsit[2]
            Counter_Loop = Counter_Loop + 1
            if Counter_Loop == rounds:
                break
        print("\n")
        if User_wins > Computer_wins:
            print("You Are The Winner!,Yay")
        else:
            print("You Lost The Game ")
        print("Game over!")


if __name__ == '__main__':

    while True:
        print("choose a statigy ..")
        choice = input("RockPlayer , RandomPlayer ,"
                       "CyclePlayer ,ReflectPlayer : ").lower()
        if choice == 'rockplayer':
            game = Game(HumanPlayer(), RockPlayer())
            game.play_game(False)
            break
        elif choice == 'randomplayer':
            game = Game(HumanPlayer(), RandomPlayer())
            game.play_game(False)
            break
        elif choice == 'cycleplayer':
            game = Game(HumanPlayer(), CyclePlayer())
            game.play_game(False)
            break
        elif choice == 'reflectplayer':
            game = Game(HumanPlayer(), ReflectPlayer())
            game.play_game(True)
            break
        else:
            print("Bad choice , please try again : ")
            continue
