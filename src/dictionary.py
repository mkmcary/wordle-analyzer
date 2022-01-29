import json

from letter import Letter


class Dictionary:
    def __init__(self, raw_word_file, five_letter_words_file, frequency_file):
        self.raw_word_file = raw_word_file
        self.output_file = five_letter_words_file
        self.frequency_file = frequency_file
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

    def read_and_filter_words(self):
        with open(self.raw_word_file, "r") as input_dict:
            with open(self.output_file, "w") as output_dict:
                word = input_dict.readline().strip()
                while word != "" and word is not None:
                    if len(word) == 5:
                        output_dict.write(word + "\n")
                        self.five_letter_words.append(word)

                    word = input_dict.readline().strip()

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
        print(letters_list)

        # Output json file
        with open(self.frequency_file, "w") as fp:
            fp.write(json.dumps(self.letter_frequencies, indent=4))


base_path = "C:\\Users\\Matthew Martin\\Documents\\NCSU Work\\PersonalProjects\\wordle-analyzer\\"
my_dict = Dictionary(
    base_path + "resources\\words_alpha.txt",
    base_path + "output\\five_letter_words.txt",
    base_path + "output\\letter_frequencies.json"
)
my_dict.read_and_filter_words()
my_dict.analyze_letter_frequency()
