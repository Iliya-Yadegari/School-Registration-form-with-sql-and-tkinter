import mysql.connector as msc

def column_save(name,LastName,birthDate,gender,ethnicity,emailAddress,entryYear,grade,semester,appliedOrNot,streetAddress,streetAddressLine2,city,state,zipCode,HomePhoneNum,CellPhoneNum):

    mydb = msc.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'schoolregform'
        )
    
    mycursor = mydb.cursor()

    sqlCommand = 'INSERT INTO student (First Name,Last Name,birth date,gender,ethnicity,email address,Entry year,grade,semester,appliedOrNot,street address,street address line 2,city,State/Province,Postal/zip code,Home Phone Number,Cell Phone number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    values = (name,LastName,birthDate,gender,ethnicity,emailAddress,entryYear,grade,
              semester,appliedOrNot,streetAddress,streetAddressLine2,city,state,
              zipCode,HomePhoneNum,CellPhoneNum)
    
    mycursor.execute(sqlCommand,values)
    mydb.commit()