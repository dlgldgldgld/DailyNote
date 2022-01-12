import sys
from DailyNote import DailyNote
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QHBoxLayout


class BasicUI ( QWidget ) : 
    def __init__ (self):
        super().__init__()
        self.InitUI()
        pass

    def setTab ( self , tabs ) : 
        dailyNote = DailyNote( )
        tabs.addTab (dailyNote , 'DailyNote')
        pass

    def InitUI ( self ) :
        m_tabs    = QTabWidget ( )
        m_hBoxLay = QHBoxLayout( )

        self.setTab( m_tabs )
        
        m_hBoxLay.addWidget(m_tabs)

        self.setLayout(m_hBoxLay)
        self.setWindowTitle('DailyNote')
        self.setGeometry( 500, 500, 500, 600 )
        self.show()
        pass


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    program = BasicUI( )
    sys.exit( app.exec_() )