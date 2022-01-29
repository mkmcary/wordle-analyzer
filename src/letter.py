class Letter:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency

    def __repr__(self):
        return self.letter + " " + str(self.frequency)
