import numpy as np

class Game(object):
    def __init__(self, id, prob_head):
        self._id = id
        self._rnd = np.random
        self._probHead = prob_head  # probability of flipping a head
        self._countWins = 0  # number of wins, set to 0 to begin
        self.n_of_flips = 20
        self._countLoss = 0

    def simulate(self, n_of_flips):

        count_tails = 0  # number of consecutive tails so far, set to 0 to begin

        # flip the coin 20 times
        for i in range(n_of_flips):

            # in the case of flipping a heads
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:  # if the series is ..., T, T, H
                    self._countWins += 1  # increase the number of wins by 1
                count_tails = 0  # the tails counter needs to be reset to 0 because a heads was flipped

            # in the case of flipping a tails
            else:
                count_tails += 1  # increase tails count by one

    def get_reward(self):
        # calculate the reward from playing a single game
        return 100*self._countWins - 250

    def get_loss_count(self):
        if self.get_reward() < 0:
            self._countLoss = 1

        return self._countLoss

class SetOfGames:
    def __init__(self, prob_head, n_games):
        self._gameRewards = [] # create an empty list where rewards will be stored
        self._lossProb = []

        # simulate the games
        for n in range(n_games):
            # create a new game
            game = Game(id=n, prob_head=prob_head)
            # simulate the game with 20 flips
            game.simulate(20)
            # store the reward
            self._gameRewards.append(game.get_reward())
            self._lossProb.append(game.get_loss_count())

    def get_ave_reward(self):
        """ returns the average reward from all games"""
        return sum(self._gameRewards) / len(self._gameRewards)

    def get_min_reward(self):
        return min(self._gameRewards)

    def get_max_reward(self):
        return max(self._gameRewards)

    def get_loss_prob(self):
        return sum(self._lossProb) / len(self._lossProb)

games = SetOfGames(prob_head=0.5, n_games=1000)
game1 = Game(id, 0.5)


print('Probability of losing $$$ when the probability of head is 0.5:',
      games.get_loss_prob())

print('Expected reward when the probability of head is 0.5:',
      games.get_ave_reward())

print('Expected MAXIMUM reward when the probability of head is 0.5:',
      games.get_max_reward())

print('Expected MINIMUM reward when the probability of head is 0.5:',
      games.get_min_reward())