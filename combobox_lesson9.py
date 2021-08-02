import sys
from PyQt5 import QtWidgets
from combobox import Ui_MainWindow


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.ui.load_items.clicked.connect(self.loadItems)
        self.ui.clear_items.clicked.connect(self.clear_item)
        self.ui.get_item.clicked.connect(self.GetItem)

        self.ui.cb_football_team.currentIndexChanged[str].connect(self.selected_changeText)
        self.ui.cb_football_team.currentIndexChanged.connect(self.selected_changeIndex)

    def selected_changeText(self, text):
        print(text)

    def selected_changeIndex(self, index):
        print(index)

    def loadItems(self):
        football_team = (["United", "City", "Dortmund", "Arsenal","Real Madrid","Barcelona","Liverpool"])
        self.ui.cb_football_team.addItems(football_team)

    def GetItem(self):
        text = self.ui.cb_football_team.currentText()
        self.ui.label_result.setText(text)


    def clear_item(self):
        self.ui.cb_football_team.clear()


def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())


create_app()