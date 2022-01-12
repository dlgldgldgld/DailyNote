import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QHBoxLayout, QMessageBox, QDialog
from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QCalendarWidget
from PyQt5.QtCore    import Qt, QDate
from NoteDBManager import NoteDBManager
from SelectionDate import SelectionDate

def CONST_ROWCNT () :
    return 4

class DailyNote_ReadMode ( QDialog ) :

    def __init__(self) :
        self.db_mng = NoteDBManager( )
        QDialog.__init__(self)
        self.__InitUI ( ) 
        pass

    def __btn_select ( self ) : 
        QMessageBox.information(self, 'MessageBox', '시작일을 입력해주세요.')
        self.startDate = SelectionDate()

        QMessageBox.information(self, 'MessageBox', '종료을 입력해주세요.')
        self.EndDate = SelectionDate()

        stDay = self.startDate.GetDate()
        edDay = self.EndDate.GetDate()
        
        self.__DisplayTable(self.db_mng.SelectDailyNoteUsingDate(stDay, edDay))

    def __btn_cancel ( self ) : 
        self.close()
        pass 

    def __GetData ( self , count ) :
        data = self.db_mng.SelectDailyNoteTopX (count)
        return data

    def __DisplayTable ( self, data ) : 
        self.noteTable.setRowCount( len ( data ) )
        for rCnt in range ( self.noteTable.rowCount() ) :
            for cCnt in range ( self.noteTable.columnCount() ) :
                item = QTableWidgetItem( str ( data [rCnt][cCnt] ) )
                item.setTextAlignment(Qt.AlignCenter)
                self.noteTable.setItem(rCnt, cCnt,item)

        self.noteTable.resizeColumnsToContents()
        self.noteTable.horizontalHeader().setStretchLastSection(True)
        pass

    def __InitUI ( self ) :
        self.noteTable = QTableWidget( 5, CONST_ROWCNT() )
        self.noteTable.setShowGrid(True)
        self.noteTable.setHorizontalHeaderLabels(["Date" ,"행복했던일" , "슬펐던일", "내일의나" ])
        self.noteTable.resizeColumnsToContents()
        self.noteTable.horizontalHeader().setStretchLastSection(True)

        data = self.__GetData( 10 )
        self.__DisplayTable( data )

        selDateBtn = QPushButton('&Select Date')
        closeBtn = QPushButton('&Close')

        selDateBtn.clicked.connect(self.__btn_select)
        closeBtn.clicked.connect(self.__btn_cancel)

        buttonHorizonLayout = QHBoxLayout( )
        buttonHorizonLayout.addWidget( selDateBtn )
        buttonHorizonLayout.addWidget( closeBtn )

        gridlayout = QGridLayout ( )
        gridlayout.addWidget( self.noteTable , 0, 0 )
        gridlayout.addLayout( buttonHorizonLayout, 1,0)

        self.setLayout(gridlayout)

        self.setWindowTitle('Read Mode')
        self.setGeometry( 1050, 500, 1200, 400 )
        self.setWindowModality( Qt.ApplicationModal )
        pass


