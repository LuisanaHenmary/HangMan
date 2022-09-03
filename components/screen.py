import tkinter as tkr

class Screen:
    #This class is for creating an object that serves as a component for the application.
    #The game screen

    """
        It is the screen that displays the game.

        __hangman: Label showing player status.
        __message: Label showing a message for the player.
        __hide_word: Label that shows the status of the hidden word.
    """

    def __init__(self, container):

        """
            Initialize the object.

            Parameters:
                self: It is to access any attribute or method of the class.
                container: Receives a widget object that is the container for everything.
        """

        self.__hangman = tkr.Label(
            container,
            background = "black",
            fg = "#a8ffa8",
            height = 10,
            width = 20
        )

        self.__hangman.grid(
            row = 0,
            columnspan = 3
        )

        self.__message = tkr.Label(
            container,
            background = "black",
            width = 20
        )

        self.__message.grid(
            row=2,
            columnspan = 3
        )

        self.__hide_word = tkr.Label(
            container,
            background = "black",
            fg = "#a8ffa8" ,
            height = 1,
            width = 20
        )

        self.__hide_word.grid(
            row = 1,
            columnspan = 3
        )

        

    def updateScreen(self, spaces, state):

        """
            Update the states of __hide_word and __hangman.

            Parameters:
                self: It is to access any attribute or method of the class.
                spaces: String containing the state of the hidden word.
                state: String containing the state of the player.
        """

        self.__hide_word["text"] = spaces
        self.__hangman["text"] = state

    def setMessage(self, message, color="black"):

        """
            Update the status of the message for the player.

            Parameters:
                self: It is to access any attribute or method of the class.
                message: String that is the message to the player.
                color: Message color.
        """
        
        self.__message.config(text=message, fg=color)