from flask import Flask
import mysql.connector
import mysql

app = Flask(__name__)

visits = 0

hello = "Hello World"

@app.route('/')
def hello_world():
   
   
   dbconnect = mysql.connector.connect(host="simplewebdbprivate.c0l2bn8ji4on.us-east-1.rds.amazonaws.com", user="admin", passwd="KtsreTyewwo1%2873", port=3306, database="simpleweb")
   cursor = dbconnect.cursor()
   sql = "INSERT INTO Visits (IsVisited, Next) Values (%s,%s)"
   val = ("1","1")
   cursor.execute(sql, val)
   dbconnect.commit()
   
   cursor.execute("SELECT COUNT(*) FROM Visits")
   count = cursor.fetchone()

   dbconnect.close()
   
   return hello+", visits on this site: "+str(count[0])+", this is development server"



if __name__ == '__main__':
   app.run(host="0.0.0.0" ,port = 7000)
