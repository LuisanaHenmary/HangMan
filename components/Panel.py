import tkinter as tkr

class Panel(tkr.LabelFrame):
    #This class is for creating an object that serves as a component for the application.
    #The control panel

    """
        It is the control panel.

        __input_letter: Field to enter a letter.
        __confirm_button: Button to confirm.
    """

    def __init__(self, container, confirm_command, reset_command):

        """
            Initialize the object.

            Parameters:
                self: It is to access any attribute or method of the class.
                container: Receives a widget object that is the container for everything.
                confirm_command: Function to confirm the entered word.
                reset_command: Function to restart the game
        """

        #Overload the parent constructor.
        super().__init__(
            container,
            text = "Panel",
            background = "black",
            fg = "#a8ffa8",
            width = 20,
            padx = 10,
            pady = 20
        )

        #Your location on the grid
        super().grid(
            row = 3,
            column = 0,
            columnspan = 3
        )

        self.__input_letter = tkr.Entry(self)

        self.__input_letter.grid(
            row = 3,
            column = 0
        )

        self.__confirm_button = tkr.Button(
            self,
            text = ">",
            command = confirm_command
        )

        self.__confirm_button.grid(
            row = 3,
            column = 1
        )

        #Enable dashboard
        self.enabled()

        #Reset button
        tkr.Button(
            self,
            text = "reset",
            command = reset_command,
            bg = "#a8ffa8",
            fg = "black"
        ).grid(row = 4)

    
    def getLetter(self):

        """
            Returns the value of the string entered.

            Parameters:
                self: It is to access any attribute or method of the class.
        """

        return self.__input_letter.get()

    def reboot(self):

        """
            Resets the text field to an empty string.

            Parameters:
                self: It is to access any attribute or method of the class.
        """

        self.__input_letter.delete(0,tkr.END)


    def enabled(self):

        """
            Change the board state to enabled.

            Parameters:
                self: It is to access any attribute or method of the class.
        """

        self.__confirm_button.config(
            state = "normal",
            bg = "#a8ffa8",
            fg = "black"
        )

        self.__input_letter.config(
            state = "normal",
            background = "#a8ffa8",
            fg = "black"
        )


    def disabled(self):
        
        """
            Change the board state to disabled.
            
            Parameters:
                self: It is to access any attribute or method of the class.
        """

        self.__confirm_button.config(
            state = "disabled",
            bg = "grey"
        )

        self.__input_letter.config(
            state = "disabled",
            bg = "grey"
        )

    