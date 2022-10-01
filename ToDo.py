

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

con = sqlite3.connect("Todo.sqlite3")
cursor = con.cursor()

cursor.execute(
    """
    Create Table if not exists Todo(
        listItem text
    )
    """
)
con.commit()
con.close()

class Ui_MainWindow(object):

    def addToList(self):
        item = self.lineEdit.text()
        if not item:
            return
        self.toDoList.addItem(item)
        self.lineEdit.setText("")

    def deleteItem(self):
        idx = self.toDoList.currentRow()
        self.toDoList.takeItem(idx)
        # self.lineEdit.setText(clicked)


    def resetList(self):
        self.toDoList.clear()

    def loadList(self):
        con = sqlite3.connect("Todo.sqlite3")
        cursor = con.cursor()
        cursor.execute("Select listItem from Todo")
        lst = cursor.fetchall()
        con.close()
        if lst:
            for item in lst:
                self.toDoList.addItem(item[0])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(325, 342)
        MainWindow.setFixedSize(325, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 8, 310, 21))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.toDoList = QtWidgets.QListWidget(self.centralwidget)
        self.toDoList.setGeometry(QtCore.QRect(7, 70, 312, 240))
        self.toDoList.setObjectName("toDoList")
        self.add = QtWidgets.QPushButton(self.centralwidget, clicked=self.addToList)
        self.add.setGeometry(QtCore.QRect(10, 40, 101, 23))
        self.add.setObjectName("add")
        self.deleteItem = QtWidgets.QPushButton(self.centralwidget, clicked=self.deleteItem)
        self.deleteItem.setGeometry(QtCore.QRect(119, 40, 100, 23))
        self.deleteItem.setObjectName("deleteItem")
        self.reset = QtWidgets.QPushButton(self.centralwidget, clicked=self.resetList)
        self.reset.setGeometry(QtCore.QRect(229, 40, 91, 23))
        self.reset.setObjectName("reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loadList()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo List"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "My ToDos"))
        self.add.setText(_translate("MainWindow", "Add To List"))
        self.deleteItem.setText(_translate("MainWindow", "Delete Item"))
        self.reset.setText(_translate("MainWindow", "Clear List"))

    def saveList(self):
        app.exec_()

        lst = [(self.toDoList.item(i).text(),) for i in range(self.toDoList.count())]
        com = """
        Insert into Todo(listItem) values (?)
        """

        con = sqlite3.connect("Todo.sqlite3")
        cursor = con.cursor()
        cursor.execute("Delete from Todo")
        cursor.executemany(com, lst)
        con.commit()
        con.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(ui.saveList())
