class Terminal:
    """
    Handles terminal operations.
    The responsibility of the Terminal class is to handle the input and output of
    the jumper code.
    Attributes:
        None
    """

    def user_response(self, message):
        """
        Gets the input (text) from the terminal and sends the message to the 
        user.
        Args:
            self (Terminal): An instance of Terminal.
            message (string): The message to display.
        Returns:
            string: The users input as a letter.
        """
        response = input(message)

        print()

        # Make sure to return the response in lower case
        return response.lower()

    def output(self, text):
        """
        Outputs the needed Terminal code.
        Args:
            self (Terminal): An instance of Terminal.
            text (variable): A variable that is used for any output needed in the game.
        """
        print(text + '\n')