import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QDialog
from PyQt5.QtWidgets import QCalendarWidget, QLineEdit, QHBoxLayout, QMessageBox
from PyQt5.QtCore    import Qt, QDate
from NoteDBManager import NoteDBManager

class DailyNote_WriteMode ( QDialog ) :

    def __init__(self) :
        self.db_mng = NoteDBManager( )
        QDialog.__init__(self)
        self.__InitUI ( ) 
        pass

    def __InitLabel ( self ) :
        # Label
        self.lbl_happy    = QLabel('Today Happy')
        self.lbl_sad      = QLabel('Today Sad')
        self.lbl_tommorow = QLabel('Tommorrow')

        self.lbl_happy.setAlignment( Qt.AlignCenter )
        self.lbl_sad.setAlignment( Qt.AlignCenter )
        self.lbl_tommorow.setAlignment( Qt.AlignCenter )

        default_fontsize = 8

        # Label Font 변경
        commonFont = self.lbl_happy.font( )
        commonFont.setPointSize(default_fontsize)
        commonFont.setBold(True)

        commonStyle = "border-color: #000000; border-style: solid; border-width: 1px"
        self.lbl_happy.setStyleSheet(commonStyle) 
        self.lbl_sad.setStyleSheet(commonStyle) 
        self.lbl_tommorow.setStyleSheet(commonStyle) 

        self.lbl_happy.setFont(commonFont)
        self.lbl_sad.setFont(commonFont)
        self.lbl_tommorow.setFont(commonFont)
        pass

    def __InitLineEdit ( self ) :

        self.lineEdit_happy    = QLineEdit( )
        self.lineEdit_sad      = QLineEdit( )
        self.lineEdit_tommorow = QLineEdit( )

        pass

    def __btn_Input ( self ) : 
        if self.lineEdit_happy.text() == "" : 
            QMessageBox.information( self, "MessageBox", "오늘 행복한 일은 뭐였어?")
            return
        elif self.lineEdit_sad.text() == "" :
            QMessageBox.information( self, "MessageBox", "오늘 슬픈일은 없었어?")
            return
        elif self.lineEdit_tommorow.text() == "" :
            QMessageBox.information( self, "MessageBox", "내일은 어떻게 살아갈거야?")
            return

        date = self.cal.selectedDate().toString('yyyy-MM-dd')
        happy = self.lineEdit_happy.text()
        sad = self.lineEdit_sad.text()
        tomorrow = self.lineEdit_tommorow.text( )

        data = [date, happy, sad, tomorrow]
        self.db_mng.UpdateDailyNote( data )
        QMessageBox.information( self, "MessageBox", "입력이 완료되었습니다!")
        pass 

    def __btn_cancel ( self ) : 
        self.close()
        pass 

    def __InitUI ( self ) :
        # Calender
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.setBaseSize(300,300)

        # Label 
        self.__InitLabel( ) 
        self.__InitLineEdit( ) 
        # Button 
        inputButton = QPushButton ( '&Write' , self ) 
        exitButton  = QPushButton ( '&Close' , self )

        inputButton.clicked.connect ( self.__btn_Input )
        exitButton.clicked.connect  ( self.__btn_cancel )

        # Layout Setting
        gridLayout   = QGridLayout( )
        buttonLayout = QHBoxLayout( )
        
        self.setLayout( gridLayout )

        gridLayout.addWidget( self.cal, 0, 0, 1, 2 )
        gridLayout.addWidget( self.lbl_happy , 1, 0 )
        gridLayout.addWidget( self.lbl_sad , 2, 0 )
        gridLayout.addWidget( self.lbl_tommorow , 3, 0 )
        
        gridLayout.addWidget( self.lineEdit_happy , 1, 1 )
        gridLayout.addWidget( self.lineEdit_sad , 2, 1 )
        gridLayout.addWidget( self.lineEdit_tommorow , 3, 1 )
        
        buttonLayout.addWidget( inputButton )
        buttonLayout.addWidget( exitButton )

        gridLayout.addLayout( buttonLayout, 4, 0 , 1, 2 )

        self.setWindowTitle('Write Mode')
        self.setGeometry( 1050, 500, 350, 300 )
        self.setWindowModality( Qt.ApplicationModal )
        pass


