from PyQt6.QtWidgets import *
from gui import *

class Main_window(QMainWindow, Ui_VoteMenu):

    """Class for Voting app"""

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.vote_button.clicked.connect(lambda: self.vote())

        self.john = 0
        self.jane = 0
        self.total = 0

        self.exit_button_2.clicked.connect(lambda: self.exit())



    def vote(self) -> None:
        """Method is for submitting a vote"""
        if self.vote_john.isChecked():
            self.intro_label.setText('You voted for John! Vote again or Exit!')
            self.john += 1
            self.total += 1
            self.exit_label.setText(f'John - {self.john}, Jane - {self.jane}, Total - {self.total}')


        elif self.vote_jane.isChecked():
            self.intro_label.setText('You Voted for Jane! Vote again or Exit!')
            self.jane += 1
            self.total += 1
            self.exit_label.setText(f'John - {self.john}, Jane - {self.jane}, Total - {self.total}')

        else:
            self.intro_label.setText('Please select a candidate before voting!')
            self.exit_label.setText(f'John - {self.john}, Jane - {self.jane}, Total - {self.total}')

    def exit(self) -> None:
        """Method is for closing the app"""
        self.close()



