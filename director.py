from jumper import Jumper
from word import Word
from terminal import Terminal

class Director:
    """The player who is playing the game.
    
    Attributes:
        _is_playing (boolean): True if game is still being played
        _lives (int): Number of lives remaining
        _jumper (Jumper): An instance of the Jumper class
        _word (Word): An instance of the Word class
        _terminal (Terminal): An instance of the Terminal class
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): An instance of Director.
        """
        self._is_playing = True

        self._lives = 5
        
        self._jumper = Jumper()

        self._word = Word()

        self._terminal = Terminal()

        self._guesses = []

        for i in range(0, len(self._word.word_choice())):
            self._guesses.append('_')
        
    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """

        while self._is_playing:
            # get parachute and use terminal to print the parachute
            self._terminal.output(self._jumper.draw_parachute())

            # displays the word with _ for words yet to be guessed
            self._terminal.output(' '.join(self._guesses))

            # collect user input
            letter = self._terminal.user_response('Guess a letter [a-z]: ')

            if letter in self._word.get_letters():
                for index, value in enumerate(self._word.get_letters()):
                    if(value == letter):
                        self._guesses[index] = letter
            else:
                self._jumper.delete_parachute()

                self._lives = self._lives - 1

            if self._lives == 0 or not '_' in self._guesses:
                self._is_playing = False
        
        self._terminal.output('Game over!')

        self._terminal.output(f'The word was: {self._word.word_choice().upper()}')

        if self._lives > 0:
            self._terminal.output('You win!!!')
        else:
            self._terminal.output('You lose!')