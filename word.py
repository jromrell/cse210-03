import random

class Word:
    """
    Provides the word for the user to guess from
    The responsibility of the word class is to pick a word from the provided
    list randomly and check to see if a letter is in the word picked.
    Attributes:
        words (list): List of words.
        selected_word (string): Picks a word at random from our provided list.
    """

    def __init__(self):
        """
        Create a list of words and pick one of them at random.
        Args:
            self (Word): An instance of Word.
        
        """
        self._words = [
        'strife', 'reflex', 'pulled', 'scale', 'malet', 'cucumber', 'zoned',
        'index', 'level', 'blurt', 'climb', 'crumble', 'fashion', 'onion', 'plain', 'computer',
        'flower', 'water', 'children', 'rainbow', 'castle', 'watermelon'
        ]

        self._selected_word = random.choice(self._words)

    def word_choice(self):
        """
        Gets the current word choice.
        Args:
            self (Word): An instance of Word.
        Returns:
            word: The current randomly chosen word from the words list.
        """
        return self._selected_word

    def get_letters(self):
        return list(self._selected_word)

    def secret_word(self, word):
        """
        Reprints the word as "_" so the user can't see the word
        Args:
            self(Word): An instance of Word.
            word(string): The randomly picked word 
        """
        word = len(self._selected_word)

        for _ in word:
            print('_')

    def check_letter(self, letter):
        """
        Checks to see if a letter exists in the selected word
        Args:
            self(Word)" An instance of Word.
            letter(boolean): randomly selected word that is then disected into individual letters
        Returns:
            True if letter is in the word,
            False if the letter is not in the word.
        """
        letters = self._selected_word

        for i in letters:
            if letter == i:
                # Found. Terminate loop by returning true
                return True

        # Above loop did not find a match so the letter doesn't exist. So returning false
        return False