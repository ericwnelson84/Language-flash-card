import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
# below is a method we used on the NATO project to take from csv format to a dictionary with French words in one
# column and english words on the other
# word_dict = {row.French: row.English for (index, row) in data.iterrows()}
else:
    word_dict = data.to_dict(orient="records")


class CardSave:

    def __init__(self):
        self.french_word = ""
        self.english_word = ""
        self.words_left = word_dict
        self.current_card = {}
        self.random_word()

    def random_word(self):
        self.current_card = random.choice(self.words_left)
        self.french_word = self.current_card["French"]
        self.english_word = self.current_card["English"]
