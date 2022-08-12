import tkinter as tkr

class MainWindow(tkr.Tk):
    #This class is for creating an object that serves as a component for the application.
    #The main window
    """
        It is the main window.
    """
    def __init__(self):
        """
            Initialize the object.

             self: It is to access any attribute or method of the class.
        """
        #Overload the parent constructor.
        super().__init__()
        #Title for the application.
        super().title("HangMan")
        #So the the size of the window does not change
        self.resizable(False,False)