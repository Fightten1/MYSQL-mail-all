#!/usr/bin/python3

try:
    import sys
    import pymysql as mydb
    from pymysql import MySQLError
    import smtplib
except ImportError as exc:
    print("Something went wrong.")
    print(exc)
    sys.exit(0)

host=input("Enter the HOST name :")
user=input("Enter the USER name for MYSQL DATABSE :")
password=input("Enter the MYSQL user password :")
database=input("Enter the DATABASE you want to connect :")

try:
    conn=mydb.connect(host,user,password,database)
    cur=conn.cursor(mydb.cursors.DictCursor)
except mydb.err.MySQLError as exc:
    print("Something went wrong.")
    print("Error Code: %d" %(exc.args[0]))
    print("Error Msg.: %s" %(exc.args[1]))
    sys.exit(0)

column="email"
tablename="test"
sql="SELECT "+column+" from "+tablename
try:
    cur.execute(sql)
except mydb.err.MySQLError as exc:
    cur.close()
    print("Error Code: %d" %(exc.args[0]))
    print("Error Msg.: %s" %(exc.args[1]))
    sys.exit(0)

row_set=cur.fetchall()
"""
while 1:
    row=cur.fetchone()
    if row is None:
        break;
    print(row[0])
"""
for row in row_set:
    print(row[column])

username=input("Enter your username: ")
password=input("Enter your password: ")
mailserver="smtp.gmail.com"
mailserverport=587
try:
    server=smtplib.SMTP(mailserver,mailserverport)
except smtplib.SMTPConnectError as exc:
    server.quit()
    print(exc)
    sys.exit(0)

try:
    server.ehlo()
    server.starttls()
    server.login(username,password)
except smtplib.SMTPAuthenticationError as exc:
    print("Error Msg.: %s" %(exc.args[1]))
    server.quit()
    sys.exit(0)
print("sdsds/n")
fromaddress="anand.joy2008@gmail.com"
'''msg=MIMEMultipart()
msg['From']=fromaddress
msg['Subject']="Python genetated email"
body="Python tst mail"
test=msg.as_string()
'''
subject="Test"
msg="xyz"

for row in row_set:

    toaddress=row[column]
    
    '''
    msg['To']=toaddress
    msg.attach(MIMEText(body,'plain'))
    server.sendmail(fromaddress,toaddress,text)
    '''
    header  = 'From: %s\n' % fromaddress
    header += 'To: %s\n' % toaddress
    header += 'Subject: %s\n\n' % subject
    msg=msg+header
    server.sendmail(fromaddress,toaddress,msg)
server.quit()




