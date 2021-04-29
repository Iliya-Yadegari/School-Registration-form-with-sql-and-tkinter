import mysql.connector as msc

def column_save():

    mydb = msc.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'myfirstdatabase'
        )
    
    mycursor = mydb.cursor()
