from urllib.parse import quote_plus
import mysql.connector

def get_connection():
    mydb = mysql.connector.connect(
        host="179.51.222.98",
        user="root",
        password="Uch@183109",
        database="vitrinev_dados",
        port="49415",
    )
    dbmysql = mydb
    return dbmysql
  
def get_sql(sql):  
    dbmysql = get_connection()
    mycursor = dbmysql.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    dbmysql.close()
    return myresult

def inserir_sql(sql, val):  
    try:
        dbmysql = get_connection()
        mycursor = dbmysql.cursor()
        mycursor.execute(sql, val)
        dbmysql.commit()
        retorno = True
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))    
        retorno = False
    finally:
        if dbmysql.is_connected():
            mycursor.close()
            dbmysql.close()
            print("MySQL connection is closed")        
            return retorno
    
