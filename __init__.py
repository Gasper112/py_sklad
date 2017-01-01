from PyQt4 import QtGui, QtCore, QtSql
 
class mainform(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.resize(600, 400)
 
        self.connect()
 
    def connect(self):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE ", "Base")
        con.setDatabaseName("./SQLiteBase/1.s3db")
 
        if not con.open():
            print ("База данных не открылась!")
            print ("-"+con.lastError().text()+"-")
            print (str(con.lastError().type()))
 
        cur = QtSql.QSqlQuery(con)
        cur.exec("SELECT * FROM One")
        print (cur.lastError().text())
 
 
        con.close()
 
 
 
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    form1 = mainform()
    form1.setWindowTitle("Работа с базами данных в PyQt4")
    form1.show()
    sys.exit(app.exec_())