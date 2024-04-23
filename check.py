import mysql.connector as connector

con = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='HARSHsql@1234',
                        database='blogpage')
cursor = con.cursor()

def check_signup(email,username,password):
    Qstr = "SELECT email FROM user WHERE email=" +"\"" + str(email) + "\""
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    if len(rows)!=0:
        if rows[0]==email:
            return False
    else:
        Qstr = "INSERT into user values(\""+str(email)+"\"," + "\"" + str(username) + "\"," + "\"" + str(password) + "\")" 
        cursor.execute(Qstr)
        con.commit()
        return True  

def check_login(email,password):
    Qstr = "SELECT email,passkey from user where email=\"" + str(email) + "\"" "and passkey=\"" + str(password) + "\""
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    if len(rows)==0:
        return False
    for row in rows:
        if (email==row[0] and password==row[1]):
            return True
    return False
          
def get_username(email,password):
    Qstr = "SELECT username from user where email=\"" + str(email) + "\"" "and passkey=\"" + str(password) + "\""
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    for row in rows:
        return row[0]    

def get_rows_content():
    Qstr = "SELECT * from blog"
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    return rows

def add_content(username,title,content):
    Qstr = "INSERT into blog VALUES(\""+str(username)+"\"," + "\"" + str(title) + "\"," + "\"" + str(content) + "\")"
    cursor.execute(Qstr)
    con.commit()
    return "sucessful insertion" 