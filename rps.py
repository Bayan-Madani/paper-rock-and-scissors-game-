

# 9
# !/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = 'k'
    their_move = 'k'

    def move(self):
        return 'rock'

#     def move2(self, my_move, their_move):
#         my_move = 'k'
#         their_move = 'k'
#         return self.move()

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        while True:
            ask = input('choice  one: rock, paper, scissors: ').lower()
            if ask in moves:
                return ask
                break
            print('Invalid.')


class ReflectPlayer(Player):
    me = 'ReflectPlayer'

    def __init__(self):
        self.count = 0

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move == 'k':
            return random.choice(moves)
        return self.their_move


#     def move2(self, my_move, their_move):
#         if self.count > 0:
#             return self.learn(my_move, their_move)


class CyclePlayer(Player):

    def move(self):
        if self.my_move == 'k':
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    count = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count = 0
#         self.move1 = []
#         self.move2 = []
        self.box1 = []
        self.box2 = []
        self.scor_of_round = {}

    def beats(self, one, two):
        while True:
            if (one != two and one in ['rock', 'scissors']
                    and two in ['rock', 'scissors']):
                if one == 'rock':
                    print('pleyer 1  is winar')
                    self.box1.append(1)
                    self.box2.append(0)
                    break
                else:
                    print('pleyer 2  is winar')
                    self.box1.append(0)
                    self.box2.append(1)
                    break
            elif (one != two and one in ['scissors', 'paper']
                  and two in ['scissors', 'paper']):
                if one == 'scissors':
                    print('pleyer 1  is winar')
                    self.box1.append(1)
                    self.box2.append(0)
                    break
                else:
                    print('pleyer 2  is winar')
                    self.box1.append(0)
                    self.box2.append(1)

                    break
            elif (one != two and one in ['rock', 'paper']
                  and two in ['rock', 'paper']):
                if one == 'paper':
                    print('pleyer 1  is winar')
                    self.box1.append(1)
                    self.box2.append(0)
                    break
                else:
                    print('pleyer 2  is winar')
                    self.box1.append(0)
                    self.box2.append(1)
                    break
            elif one == two:
                print('pleyer 1 is equal pleyer 2')
                self.box1.append(0)
                self.box1.append(0)

                break
            else:
                print('ente')
                print(one, two)
                break

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.beats(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def General_scores(self):
        print('#===========#')
        print("General_scores")
        print('#===========#')
        print("Score: player One= " + str(sum(self.box1)))
        print('Score: Player Two= ' + str(sum(self.box2)))
        print('#===========#')
        print()
        if sum(self.box1) > sum(self.box2):
            print('\n player 1 is winr in the game')
        elif sum(self.box1) < sum(self.box2):
            print('\n player 2 is winr in the game')
        else:
            print('\n we have two winers!')
        print("Game over!")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            number_round = f"Round {round}:"
            print(number_round)
            self.play_round()
            print('Score: player One ' +
                  str(sum(self.box1)),
                  ' score: Player Two ' + str(sum(self.box2)))
            self.count += 1
            self.scor_of_round[number_round] = ("#===========#"
                                                "\n #===========#"
                                                "\n Score: player One= "
                                                + str(sum(self.box1))
                                                + "\n Score: Player Two= "
                                                + str(sum(self.box2))
                                                + "\n #===========#")
            if sum(self.box1) == 3 or sum(self.box2) == 3:
                break
        for round_n, score in self.scor_of_round.items():
            print(f"\n Current {round_n}")
            print(score)
        self.General_scores()

    def play_game_1round(self):
        print("Game start!")
        for round in range(1):
            number_round = f"Round {round}:"
            print(number_round)
            self.play_round()
            print('Score: player One ' +
                  str(sum(self.box1)),
                  ' score: Player Two ' + str(sum(self.box2)))
            self.count += 1
            self.scor_of_round[number_round] = ("#===========#"
                                                "\n #===========#"
                                                "\n Score: player One= "
                                                + str(sum(self.box1))
                                                + "\n Score: Player Two= "
                                                + str(sum(self.box2))
                                                + "\n #===========#")
            if sum(self.box1) == 3 or sum(self.box2) == 3:
                break
        for round_n, score in self.scor_of_round.items():
            print(f"\n Current {round_n}")
            print(score)
        self.General_scores()


if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']
    # players = [
    #     AllRockPlayer(),
    #     RandomPlayer(),
    #     ReflectPlayer(),
    #     CyclePlayer()
    # ]
    # p1 = HumanPlayer()
    # p2 = random.choice(players)
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
#     game.play_game_1round()
