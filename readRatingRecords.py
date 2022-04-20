from dbConnect import *
import time

def readRatingRecords():
  print("What rating you are looking for?")
  print("Pick one or more from list below")
  cursor.execute(f"SELECT DISTINCT rating FROM tblFilms")
  ratingList = (
    cursor.fetchall()
  )

  for rating in ratingList:
    print(rating)
  ratingRercord = input("Which rating would you like to see? ").upper()
  ratingRercord = "'" + ratingRercord + "'"
  cursor.execute(f"SELECT * FROM tblFilms WHERE rating={ratingRercord}")
  row = (
    cursor.fetchall()
  )
  for rating in row:
    time.sleep(0.5)
    print(rating)
readRatingRecords()