# create a database and add input & output
import os, sqlite3

def writeToDatabase(myinput, myoutput):
    path = os.getcwd()

    if not os.path.exists(path+'/database/'):
        os.mkdir(path+'/database/')

    # create database if first time
    # columns: id, input, output
    if not os.path.isfile(path+'/database/hoover_db.db'):
        connection = sqlite3.connect(path+'/database/hoover_db.db')
        cursor = connection.cursor()
        sql_command = 'CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, input VARCHAR(500), output VARCHAR(50));'
        cursor.execute(sql_command)
    else:
        connection = sqlite3.connect(path+'/database/hoover_db.db')
        cursor = connection.cursor()

    parameters = (str(myinput), str(myoutput))
    cursor.execute('INSERT INTO data VALUES (NULL, ?, ?)', parameters)

    connection.commit()
    connection.close()
