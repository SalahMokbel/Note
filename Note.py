import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QListWidget, QListWidgetItem, QTextEdit, QTextBrowser
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, pylupdate
import os

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "new app"
        self.left = 200
        self.top = 150
        self.width = 260
        self.height = 180

        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 5, 200, 40))
        self.label.setFont(font)

        # User name
        self.label1 = QLabel(self)
        self.label1.setGeometry(QtCore.QRect(40, 55, 100, 15))
        self.User_name = QLineEdit(self)
        self.User_name.setGeometry(QtCore.QRect(100, 53, 120, 20))

        # Password
        self.label2 = QLabel(self)
        self.label2.setGeometry(QtCore.QRect(45, 80, 100, 15))
        self.Password = QLineEdit(self)
        self.Password.setGeometry(QtCore.QRect(100, 78, 120, 20))

        # Enter Button
        self.Enter = QPushButton(self)
        self.Enter.setGeometry(QtCore.QRect(80, 103, 120, 30))
        self.Enter.clicked.connect(self.enter)

        # Register Button
        self.Register = QPushButton(self)
        self.Register.setGeometry(QtCore.QRect(180, 150, 80, 30))
        self.Register.setText("Register")
        self.Register.clicked.connect(self.screen)

        # Error label
        error_label_font = QFont()
        error_label_font.setBold(True)
        error_label_font.setWeight(20)
        error_label_font.setFamily("MS Shell Dlg 2")
        error_label_font.setPointSize(10)
        self.label_error = QLabel(self)
        self.label_error.setGeometry(60, 128, 170, 30)
        self.label_error.setFont(error_label_font)


        self.initUI()

    def screen(self):
        Form2.show()


    def enter(self):

        user_name_info = self.User_name.text()
        password_info = self.Password.text()

        os.chdir("C:/Users/broye97/Desktop/untitled/Passwords")
        info = os.listdir()
        if user_name_info in info:
            file = open(user_name_info, "r")
            v = file.read().splitlines()
            if password_info in v:
                print("login")
                self.User_name.clear()
                self.Password.clear()
                self.label_error.setText("login...")
                self.label_error.setGeometry(120, 133, 100, 30)
                Form.show()

            else:
                print("password has not recognised")
                self.label_error.setText("password has not recognised")

        else:
            print("user name not fond")
            self.label_error.setText("user name not fond")


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label.setText("WELCOME")
        self.label1.setText("User Name:")
        self.label2.setText("Password:")
        self.Enter.setText("ENTER")
        self.show()

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.resize(360, 240)
        Form.setWindowTitle("Note's")

        Font = QFont()
        Font.setBold(True)
        Font.setPointSize(16)
        Font.setWeight(75)

        # add button
        self.add = QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(5, 5, 55, 27))
        self.add.setText("NEW")
        self.add.clicked.connect(self.new_note)

        font = QFont()
        font.setBold(True)
        font.setPointSize(10)

        self.label = QLabel(Form)
        self.label.setGeometry(8, 37, 50, 20)
        self.label.setText("Note's:")
        self.label.setFont(font)

        self.listWidget = QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(5, 57, 80, 180))
        self.listWidget.setObjectName("listWidget")
        # self.listWidget.itemClicked.connect(self.viewNote)


        self.open_note = QLabel(Form)
        self.open_note.setGeometry(115, 3, 80, 30)
        self.open_note.setText("Note Name:")
        self.open_note.setFont(font)

        self.open_entry = QLineEdit(Form)
        self.open_entry.setGeometry(QtCore.QRect(190, 8, 100, 20))

        self.open_button = QPushButton(Form)
        self.open_button.setGeometry(QtCore.QRect(295, 5, 60, 25))
        self.open_button.setText("OPEN")
        self.open_button.clicked.connect(self.viewNote)

        self.label2 = QTextBrowser(Form)
        self.label2.setGeometry(90, 40, 260, 197)

        self.refrish_button = QPushButton(Form)
        self.refrish_button.setGeometry(QtCore.QRect(60, 5, 35, 30))
        self.refrish_button.setText("R")
        self.refrish_button.clicked.connect(self.refresh)

        self.lwidget()

    def viewNote(self):

        name = self.open_entry.text()
        os.chdir("C:/Users/broye97/Desktop/untitled/Note's")
        file = os.listdir()
        if name in file:
            f = open(name, "r")
            v = f.read()
            self.label2.setText(v)
        else:
            print("There is No Note's under this name")


    def lwidget(self):

        os.chdir("C:/Users/broye97/Desktop/untitled/Note's")

        notes = os.listdir()
        for i in notes:
            item = QListWidgetItem()
            self.listWidget.addItem(item)
            item.setText(i)

    def refresh(self):

        self.listWidget.clear()
        os.chdir("C:/Users/broye97/Desktop/untitled/Note's")
        notes = os.listdir()
        for i in notes:
            item = QListWidgetItem()
            self.listWidget.addItem(item)
            item.setText(i)


    def new_note(self):
        Form3.show()

class newNote(QWidget):
    def setUpNewNote(self, Form3):
        Form3.resize(360, 240)
        Form3.setWindowTitle("New Note")

        font = QFont()
        font.setBold(True)
        font.setPointSize(8)

        self.label = QLabel(Form3)
        self.label.setGeometry(130, 10, 80, 20)
        self.label.setText("Note Name:")
        self.label.setFont(font)

        self.notename = QLineEdit(Form3)
        self.notename.setGeometry(QtCore.QRect(200, 10, 120, 20))

        self.input = QTextEdit(Form3)
        self.input.setGeometry(20, 40, 320, 190)

        self.savebutton = QPushButton(Form3)
        self.savebutton.setGeometry(20, 8, 40, 30)
        self.savebutton.setText("SAVE")
        self.savebutton.clicked.connect(self.saveNote)

    def saveNote(self):

        note_name = self.notename.text()
        note = self.input.toPlainText()

        self.notename.clear()
        self.input.clear()

        os.chdir("C:/Users/broye97/Desktop/untitled/Note's")
        note_info = open(note_name, "w")
        note_info.write(note)
        note_info.close()
        print("SAVED")

class Register(QWidget):
    def setup(self, Form2):

        font2 = QFont()
        font2.setWeight(75)
        font2.setPointSize(16)
        font2.setBold(True)

        Form2.resize(280, 210)
        Form2.setWindowTitle("Registration")

        self.label = QLabel(Form2)
        self.label.setGeometry(100, 20, 100, 40)
        self.label.setText("Register")
        self.label.setFont(font2)

        # user name
        self.user_name = QLabel(Form2)
        self.user_name.setGeometry(55, 72, 60, 20)
        self.user_name.setText("User name:")
        self.username_entry1 = QLineEdit(Form2)
        self.username_entry1.setGeometry(QtCore.QRect(125, 75, 120, 20))

        # password
        self.password = QLabel(Form2)
        self.password.setGeometry(60, 100, 60, 20)
        self.password.setText("Password:")
        self.password_entry2 = QLineEdit(Form2)
        self.password_entry2.setGeometry(QtCore.QRect(125, 100, 120, 20))

        # confirm password
        self.confirm_password = QLabel(Form2)
        self.confirm_password.setGeometry(22, 125, 90, 20)
        self.confirm_password.setText("Confirm password:")
        self.confirmpassword_entry3 = QLineEdit(Form2)
        self.confirmpassword_entry3.setGeometry(QtCore.QRect(125, 125, 120, 20))

        # Register Button
        self.Register = QPushButton(Form2)
        self.Register.setGeometry(QtCore.QRect(100, 160, 110, 40))
        self.Register.setText("Register")
        self.Register.clicked.connect(self.register_button)

    def register_button(self):

        username = self.username_entry1.text()
        password = self.password_entry2.text()
        confirmpassword = self.confirmpassword_entry3.text()

        os.chdir("C:/Users/broye97/Desktop/untitled/Passwords")


        if confirmpassword == password:
            info_file = open(username, "w")
            info_file.write(password)
            info_file.close()
            print("saved")
        else:
            print("password not mach")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()

    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    Form2 = QWidget()
    ui2 = Register()
    ui2.setup(Form2)

    Form3 = QWidget()
    ui3 = newNote()
    ui3.setUpNewNote(Form3)

    sys.exit(app.exec_())


