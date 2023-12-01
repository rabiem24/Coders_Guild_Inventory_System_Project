import pymysql

# Open database connection
db = pymysql.connect("localhost", "admin", "admin", "HELLO")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS Hi")

# Create table as per requirement
sql = """CREATE TABLE Hi (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()