# import mysql.connector
#
# mydb = mysql.connector.connect(host='200.239.92.223', user='root', password='')
#
# print(mydb)

import mysql.connector
from mysql.connector import errorcode
# from sqlalchemy import create_engine
# engine = create_engine('mysql+mysqldb://root@localhost/fastssr')
# Obtain connection string information from the portal

config = {
  'host':'localhost',
  'user':'root',
  'password':'',
  'database':'FASTSSR'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
# else:
#   cursor = conn.cursor()

  # Read data
  # cursor.execute("SELECT * FROM CONSULTA;")
  # rows = cursor.fetchall()
  # print("Read",cursor.rowcount,"row(s) of data.")

  # Print all rows
  # for row in rows:
  # 	print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")
