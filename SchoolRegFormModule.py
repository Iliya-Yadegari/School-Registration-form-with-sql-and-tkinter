import mysql.connector as msc

def column_save(name,LastName,birthDate,gender,ethnicity,emailAddress,entryYear,grade,semester,appliedOrNot,streetAddress,streetAddressLine2,city,state,zipCode,HomePhoneNum,CellPhoneNum):

    mydb = msc.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'schoolregform'
        )
    
    mycursor = mydb.cursor()

    sqlCommand = 'INSERT INTO resultsv2 (Name,LastName,Birthdate,Gender,Ethnicity,EntryYear,Grade,Semester,appliedOrNot,StreetAddress,StreetAddressLine2,City,State,PostalNum,HomePhoneNum,CellPhoneNum) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    values = (name,LastName,birthDate,gender,ethnicity,emailAddress,entryYear,grade,
              semester,appliedOrNot,streetAddress,streetAddressLine2,city,state,
              zipCode,HomePhoneNum,CellPhoneNum)
    
    mycursor.execute(sqlCommand,values)
    mydb.commit()