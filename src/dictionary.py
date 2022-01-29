import json

from letter import Letter
from word import Word


class Dictionary:
    def __init__(self, raw_word_file, five_letter_words_file, frequency_file, ranked_words_file):
        self.raw_word_file = raw_word_file
        self.output_file = five_letter_words_file
        self.frequency_file = frequency_file
        self.ranked_words_file = ranked_words_file
        self.five_letter_words = []
        self.letter_frequencies = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }
        self.ranked_letters = []
        self.ranked_words = []

    def read_and_filter_words(self):
        print("Reading in raw dictionary from " + self.raw_word_file)
        with open(self.raw_word_file, "r") as input_dict:
            with open(self.output_file, "w") as output_dict:
                word = input_dict.readline().strip()
                while word != "" and word is not None:
                    if len(word) == 5:
                        output_dict.write(word + "\n")
                        self.five_letter_words.append(word)

                    word = input_dict.readline().strip()
        print("Output list of five letter words to " + self.output_file)

    def analyze_letter_frequency(self):
        raw_frequencies = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }

        print("\nAnalyzing letter frequency from five letter words.")

        # Add all the raw occurrences of each letter
        total_letters = 0
        for word in self.five_letter_words:
            for char in word:
                raw_frequencies[char] += 1
                total_letters += 1

        # Standardize
        letters_list = []
        for letter in raw_frequencies:
            frequency = raw_frequencies[letter] / total_letters
            self.letter_frequencies[letter] = frequency
            letters_list.append(Letter(letter, frequency))

        letters_list.sort(key=(lambda let: let.frequency), reverse=True)
        self.ranked_letters = letters_list

        # Output json file of letter frequencies
        with open(self.frequency_file, "w") as fp:
            fp.write(json.dumps(self.letter_frequencies, indent=4))

        print("Frequency of letters determined:")
        print(json.dumps(self.letter_frequencies, indent=4))

        print("\nRanking of Letters:")
        for i in range(1, 27):
            print(str(i) + ". " + letters_list[i - 1].letter)

    def score_all_words(self):
        for word in self.five_letter_words:
            score = self.calculate_score_for_word(word)
            self.ranked_words.append(Word(word, score))

        self.ranked_words.sort(key=(lambda word: word.score), reverse=True)
        print("Ranked Words Top 5:")
        for i in range(5):
            print(str(i) + ". " + self.ranked_words[i].word)

        with open(self.ranked_words_file, "w") as fp:
            ranked_dict = {}
            for word in self.ranked_words:
                ranked_dict[word.word] = word.score

            fp.write(json.dumps(ranked_dict, indent=4))

    def calculate_score_for_word(self, word):
        # Give score for each letter in the word by frequency
        frequency_score = 0
        for letter in word:
            frequency_score += self.letter_frequencies[letter] * 100

        # Check letter diversity
        unique_letters = []
        for letter in word:
            if letter not in unique_letters:
                unique_letters.append(letter)

        diversity_score = len(unique_letters) * 10

        # Letter placement score?

        return frequency_score + diversity_score
