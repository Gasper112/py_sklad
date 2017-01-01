__author__ = 'Андрюсик'
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3

conn = sqlite3.connect('sklad.db')
c = conn.cursor()

c.execute('SELECT * FROM items')
data = c.fetchall()
print (data)


def create_table(data):
    tab = QTableView()
    headers = []

    c.execute('PRAGMA TABLE_INFO(items);')
    buf = c.fetchall()
    for item in buf:
        headers.append(item[1])

    tm = MyTableModel(data, headers, tab)
    tab.setModel(tm)

    # set the minimum size
    tab.setMinimumSize(400, 300)

        # hide grid
    tab.setShowGrid(True)

        # set the font
    font = QFont("Courier New", 8)
    tab.setFont(font)

        # hide vertical header
    vh = tab.verticalHeader()
    vh.setVisible(False)

        # set horizontal header properties
    hh = tab.horizontalHeader()
    hh.setStretchLastSection(True)

        # set column width to fit contents
    tab.resizeColumnsToContents()

        # set row height
    nrows = len(data)

    for row in range(nrows):
        tab.setRowHeight(row, 18)

    return tab




class MyTableModel(QAbstractTableModel):
    def __init__(self, data, headers, parent = None, *args):
        QAbstractTableModel.__init__(self,parent,*args)
        self.data = data
        self.headers = headers

    def rowCount( self, parent=None):
        return len(self.data)

    def columnCount(self, parent=None):
        return len(self.data[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.data[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[col]
        return None

class GridLayout(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle('grid layout')

        title = QLabel('Title')
        author =QLabel('Author')
        review =QLabel('Review')
        test1 = QLabel('Test1')
        test2 = QLabel('Test2')
        test3 = QLabel('Test3')

        titleEdit = QLineEdit()
        authorEdit =QLineEdit()
        table = create_table(data)

        grid = QGridLayout()
        grid.setSpacing(15)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(test1, 1, 2)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(test2, 2, 2)

        grid.addWidget(review, 3, 0)
        grid.addWidget(table, 3, 1)

        grid.addWidget(test3, 9, 0)


        self.setLayout(grid)
        self.resize(800, 300)



app = QApplication(sys.argv)
qb = GridLayout()
qb.show()
sys.exit(app.exec_())