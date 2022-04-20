from dbConnect import *
import time

def readYearRecords():
  yearReleased = int(input("From what year would you like to see the films? "))
  print(type(yearReleased))
  cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased={yearReleased}")

  row = (
    cursor.fetchall()
  )
  for record in row:
    time.sleep(1)
    print(record)

readYearRecords()