from json import JSONEncoder


class Word(JSONEncoder):
    def __init__(self, word, score):
        self.word = word
        self.score = score
