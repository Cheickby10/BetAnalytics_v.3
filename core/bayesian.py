from scipy.stats import beta

class EdgeEstimator:
    def __init__(self):
        self.wins = 1
        self.losses = 1

    def update(self, win):
        if win:
            self.wins += 1
        else:
            self.losses += 1

    def estimate(self):
        return beta.mean(self.wins, self.losses)
