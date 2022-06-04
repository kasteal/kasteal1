import sqlite3 as sl
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import sys


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super().__init__()
        self.setupUi(self)
        self.best_2.setPlaceholderText('Лучшая аниме тян')
        self.name.setPlaceholderText('Имя новой тян')
        self.ann.setPlaceholderText('Информация о работе программы')

        self.best.clicked.connect(lambda: self.best_tyan())
        self.rem.clicked.connect(lambda: self.remove())
        self.add.clicked.connect(lambda: self.new_girl())

    def new_girl(self):
        a = self.name.text()
        value = self.ball.text()
        if a == '' or value == '' or not value.isdigit():
            self.ann.setText('Недостаточность/некорректность данных')
        else:
            con = sl.connect('basa.db')
            cur = con.cursor()
            with con:
                cur.execute('INSERT INTO tyan VALUES(?,?)', (a, value))
                con.commit()
                self.ann.setText('Данные добавлены')
        self.clear()

    def remove(self):
        a = self.name.text()
        con = sl.connect('basa.db')
        cur = con.cursor()
        all_tyan = cur.execute('SELECT * FROM tyan')
        f = 0
        for tyan in all_tyan:
            if a in tyan:
                with con:
                    cur.execute('DELETE FROM tyan WHERE name == ?;', (a, ))
                    con.commit()
                    self.ann.setText('Данные удалены')
            else:
                self.ann.setText('Ее и не было')
        self.clear()

    def best_tyan(self):
        con = sl.connect('basa.db')
        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM tyan')
            all_tyan = cur.fetchall()
        if all_tyan == []:
            self.ann.setText('В бд ничего нет')
        else:
            all_tyan.sort(key = lambda x: (x[0], x[1]))
            self.best_2.setText(all_tyan[0][0])
            self.ann.setText('Вот она')

    def clear(self):
        self.name.setText('')
        self.ball.setText('')


app = QtWidgets.QApplication(sys.argv)


if __name__ == '__main__':
    con = sl.connect('basa.db')
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS tyan(
            name TEXT,
            value INTEGER
        )''')
    win = Window()
    win.show()

    sys.exit(app.exec())
