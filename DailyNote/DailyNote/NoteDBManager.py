
import sqlite3

def CONST_DBNAME( ) :
    return "db/dailynote.db"

class NoteDBManager ( ) :
    def __init__ ( self ) :
        self.conn = sqlite3.connect( CONST_DBNAME ( ) )
        self.db_cursor = self.conn.cursor()
        self.__CreateTable ()
        pass

    def __del__(self):
        self.conn.close( )

    # DailyNote Update
    def UpdateDailyNote ( self, data ) :

        date = data[0]
        happy = data[1]
        sad = data[2]
        tomorrow = data[3]
        
        rows = self.SelectDailyNote( date )

        query = '';
        if len(rows) == 0 : 
            #insert
            query = "INSERT INTO DAILYNOTE VALUES ( :date , :happy, :sad , :tomorrow )"
            pass
        else : 
            #update Date
            query = "UPDATE DAILYNOTE SET happything = :happy, sadthing = :sad, tomorrow = :tomorrow WHERE date = :date"
            pass

        self.db_cursor.execute( query, { "date" : date, "happy" : happy, "sad" : sad, "tomorrow" : tomorrow } )
        self.conn.commit()
        pass

    # DailyNote Select 
    def SelectDailyNote ( self, date ) :
        query = "SELECT * FROM DAILYNOTE WHERE date = ?"
        self.db_cursor.execute( query, (date, ) )
        rows = self.db_cursor.fetchall()
        return rows
        pass

    # DailyNote Select 
    def SelectDailyNoteTopX ( self, limit ) :
        query = "SELECT * FROM DAILYNOTE ORDER BY date DESC LIMIT ?  "
        self.db_cursor.execute( query, ( limit, ) )
        rows = self.db_cursor.fetchall()
        return rows
        pass

    def SelectDailyNoteUsingDate(self, start, end ) :
        query = "SELECT * FROM DAILYNOTE where DATE(date) BETWEEN ? AND ? ORDER BY date ASC"
        self.db_cursor.execute( query, ( start, end,  ) )
        rows = self.db_cursor.fetchall()
        return rows
        pass
        
    # Create Table If table is not exists in current Environment.
    def __CreateTable ( self )  : 
        query = """ 
            CREATE TABLE IF NOT EXISTS DAILYNOTE 
            ( 
                date TEXT not null ,
                happything TEXT not null,
                sadthing TEXT not null,
                tomorrow TEXT not null
            )
            """
        self.db_cursor.execute( query )
        pass

if __name__ == '__main__' :
    dbMng = NoteDBManager( )

