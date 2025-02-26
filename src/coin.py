import random


# The coin class simulates a coin that can
# be flipped

class Coin:

    # The __init__ method initializes the
    # side up data attribute with 'Heads'.

    def __init__(self):
        self.sideup = 'Heads'

    # The Toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get sideup method returns the value
    # referenced by sideup

    def get_sideup(self) -> str:
        """
        It returns which side is facing up when the coin lands. I.e. heads or tails.
        :return: str: `Heads or Tails`
        """
        return self.sideup