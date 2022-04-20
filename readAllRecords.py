from dbConnect import *
import time

def readAllRecords():
  cursor.execute("SELECT * FROM tblFilms")

  row = (
    cursor.fetchall()
  )
  for film in row:
    print(film)

readAllRecords()