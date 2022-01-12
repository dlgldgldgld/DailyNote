import sys
from DailyNote_WriteMode import DailyNote_WriteMode
from DailyNote_ReadMode import DailyNote_ReadMode
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QDialog
from PyQt5.QtGui     import QPixmap
from PyQt5.QtCore    import Qt


class DailyNote ( QWidget ) :

    def __init__ ( self ) : 
        super().__init__()
        self.__InitUI( )
        pass

    def __SetButton ( self ) :
        self.writeMode = QPushButton( '&Write Mode' )
        self.ReadMode  = QPushButton( '&Read Mode' )
        self.CloseMode = QPushButton( '&Close')
        
        self.writeMode.clicked.connect(self.__Click_Write)
        self.ReadMode.clicked.connect (self.__Click_Read)
        self.CloseMode.clicked.connect(self.__Click_Close)
        pass

    def __SetOtherComponent ( self ) :
        # PixMap setting 
        self.pixmap = QPixmap('img/DailyNote_Back.jpg')
        self.pixmap = self.pixmap.scaledToWidth( 500 )

        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(self.pixmap)

        pass

    def __Click_Write( self ):
        # dialog 를 선언한 후에 Show를 진행.
        self.write_dialog = DailyNote_WriteMode( )
        self.write_dialog.show( )
        pass

    def __Click_Read( self ):
        self.read_dialog = DailyNote_ReadMode( )
        self.read_dialog.show( )
        pass

    def __Click_Close(self):
        sys.exit()
        pass

    def __InitUI ( self ) :

        gridLayout = QGridLayout()
        self.setLayout( gridLayout )
        
        self.__SetButton()
        self.__SetOtherComponent()

        gridLayout.addWidget(self.lbl_img,   0, 0, 1, 2 )
        gridLayout.addWidget(self.writeMode, 1, 0 )
        gridLayout.addWidget(self.ReadMode,  1, 1 )
        gridLayout.addWidget(self.CloseMode, 2, 1 )
        
        
        self.show()
        pass



