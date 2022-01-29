class GuessInfo:
    def __init__(self, known_characters, contains_characters, invalid_characters):
        self.known_characters = known_characters
        self.contains_characters = contains_characters
        self.invalid_characters = invalid_characters

    def is_valid(self, letter, position):
        # Is this character known to be invalid?
        if letter in self.invalid_characters:
            return False

        # Is this position occupied by another known character?
        if (self.known_characters[position] is not None) and (self.known_characters[position] != letter):
            return False

        return True

    def is_word_valid(self, word):
        # Check if the letters are valid
        for i in range(5):
            letter = word[i]
            if not self.is_letter_valid(letter, i):
                return False


        if not invalid:
            new_ranked_words.append(word_obj)
