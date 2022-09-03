import random
from components.main_window import MainWindow
from components.screen import Screen
from components.Panel import Panel

class App:

    """
      This class is the union of the components of the 
      application and who manages its operation.
    
      __attemps: Integer representing the number of attempts for the player
      __spaces: String containing the state of the hidden word.
      __word: String that is the chosen word.
      __states: List of strings where each is a state for the hangman.
      __DB: List of words where only one will be chosen as the hidden word.
    """



    __attemps = 0
    __spaces = ""
    __word = ""
    __states = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''' ,'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''' , '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''' ,'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''' , '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

    __DB  = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

    def __init__(self):

        """
          Initialize the object.

          Parameters:
            self: It is to access any attribute or method of the class.
        """

        self.__window = MainWindow()
        self.__view = Screen(self.__window)

        self.__resp = Panel(
          self.__window,
          confirm_command = self.confirm,
          reset_command=self.begin
        )

        self.begin()
        self.__window.mainloop()



    def begin(self):

      """
        It is to give the game an initial state.

        Parameters:
            self: It is to access any attribute or method of the class.
      """
    
      self.__attemps = 6
      self.__word = random.choice(self.__DB)
      self.__spaces = ["_"]*len(self.__word)
      
      self.__view.updateScreen(
        spaces = self.__spaces,
        state = self.__states[self.__attemps]
      )

      self.__view.setMessage("")
      self.__resp.enabled()

    def validation(self):

      """
        It is to verify if what is entered is only a letter,
        and if so, to validate if the letter belongs to the hidden word.
        
        Parameters:
            self: It is to access any attribute or method of the class.
      """

      self.__view.setMessage("")
      found = False

      if len(self.__resp.getLetter()) == 0 or len(self.__resp.getLetter()) > 1:
        self.__resp.reboot()
        self.__view.setMessage("Write only one letter","#f5010a")
        return

      for index, charater in enumerate(self.__word):
        
          if charater == self.__resp.getLetter():
            self.__spaces[index] = self.__resp.getLetter()
            found = True
          
      if not found:
        self.__attemps -= 1
      self.__resp.reboot()

    def verification(self):

      """
        Check if the number of attempts reached zero or if there 
        are no more blanks.
      
        Parameters:
            self: It is to access any attribute or method of the class.
      """

      if(self.__attemps == 0):

        for index, charater in enumerate(self.__word):
          self.__spaces[index] = charater

        self.__view.setMessage("GAMER OVER","#f5010a")
        self.__resp.disabled()
        return

      if("_" not in self.__spaces):
        self.__view.setMessage("WIN YOU","#a8ffa8")
        self.__resp.disabled()
        return

    def confirm(self):

      """
        Validates the letter entered, checks if there are zero attempts or
        if the word has already been discovered, and updates the screen.

        Parameters:
            self: It is to access any attribute or method of the class.
      """

      self.validation()
      self.verification()
      self.__view.updateScreen(self.__spaces, self.__states[self.__attemps])
      

      

    

