from dbConnect import *
import time
def readGenreRecords():
  listOfGenre = ["Comedy", "Test", "Action", "Crime", "Animation", "Fantasy", "Fighting"]
  print("Full list of film genre available:")
  for genre in listOfGenre:
    time.sleep(0.5)
    print(genre)
  genreType = input("What type of film you are looking for? ").title()
  genreType = "'" + genreType + "'"
  cursor.execute( f"SELECT * FROM tblFilms WHERE genre={genreType}" )
  row = (
    cursor.fetchall()
  )
  for record in row:
    time.sleep(1)
    print(record)

readGenreRecords()