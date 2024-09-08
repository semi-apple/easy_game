import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Guess Number Game')
        self.setGeometry(100, 100, 300, 200)

        self.secret_number = random.randint(0, 9)
        self.attempts = 0

        self.label = QLabel('I am thinking of a number between 1 and 100. Guess it!', self)
        self.input_label = QLabel('Enter your guess (0-9):', self)
        self.input_box = QLineEdit(self)
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.check_guess)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def check_guess(self):
        try:
            guess = int(self.input_box.text())
            self.attempts += 1

            if guess < self.secret_number:
                QMessageBox.information(self, 'Guess Number Game', 'Too low, try again.')
            elif guess > self.secret_number:
                QMessageBox.information(self, 'Guess Number Game', 'Too high, try again.')
            else:
                QMessageBox.information(self, 'Guess Number Game', f'Congratulations, you guessed it right! You took {self.attempts} attempts.')
                self.reset_game()

            self.input_box.clear()

        except ValueError:
            QMessageBox.warning(self, 'Guess Number Game', 'Please enter a valid number!')

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    game.show()
    sys.exit(app.exec_())
