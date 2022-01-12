import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QHBoxLayout, QMessageBox, QDialog
from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtCore    import Qt, QDate, QEventLoop

class SelectionDate( QDialog ) :
    def __init__ (self) :
        QDialog.__init__(self)

        self.event_loop = QEventLoop()

        self.__InitUI()
        self.show()
        self.event_loop.exec_()
        pass
    
    def GetDate(self) : 
        return self.date

    def __btn_input(self):
        self.date = self.calender.selectedDate().toString('yyyy-MM-dd')
        self.close()
        self.event_loop.exit()

    def __btn_close(self):
        self.close()
        pass

    def __InitUI ( self ) :
        self.calender = QCalendarWidget( )

        input_Btn = QPushButton('입력')
        close_Btn = QPushButton('종료')

        input_Btn.clicked.connect(self.__btn_input)
        close_Btn.clicked.connect(self.__btn_close)

        gridLayout = QGridLayout()
        gridLayout.addWidget( self.calender, 0, 0 )
        
        btnHorizonLayout = QHBoxLayout()
        btnHorizonLayout.addWidget ( input_Btn )
        btnHorizonLayout.addWidget ( close_Btn )

        gridLayout.addLayout( btnHorizonLayout, 1, 0)
        self.setLayout(gridLayout)

        self.setWindowTitle('Select Date')
        self.setGeometry( 1050, 500, 300, 300 )
        self.setWindowModality( Qt.ApplicationModal )


        
