from dictionary import Dictionary
from guess_info import GuessInfo
from word import Word


class WordleAnalyzer:
    def __init__(self):
        base_path = "C:\\Users\\Matthew Martin\\Documents\\NCSU Work\\PersonalProjects\\wordle-analyzer\\"
        self.dictionary = Dictionary(
            base_path + "resources\\words_alpha.txt",
            base_path + "output\\five_letter_words.txt",
            base_path + "output\\letter_frequencies.json",
            base_path + "output\\ranked_words.json"
        )
        self.dictionary.read_and_filter_words()
        self.dictionary.analyze_letter_frequency()
        self.dictionary.score_all_words()

    def best_five_words(self, guess_info):
        # Filter out invalid words
        new_ranked_words = []
        for word_obj in self.dictionary.ranked_words:
            word = word_obj.word
            # Assume validity


        # Sort for assurance
        new_ranked_words.sort(key=(lambda w: w.score), reverse=True)

        print("Ranked Words Top 5:")
        for i in range(5):
            print(str(i) + ". " + new_ranked_words[i].word)
        return []


# Create a new WordleAnalyzer
wa = WordleAnalyzer()

print("################################################")
gi = GuessInfo([None, None, None, None, None], ["a", "o", "s"])
print(wa.best_five_words(gi))
