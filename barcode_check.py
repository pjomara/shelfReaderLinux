import sqlite3
import time
import datetime
import sys
import os

def main():

    barcode = input ("Scan the first barcode: ")
    barcode_check(barcode)

def barcode_check(barcode):
    conn = sqlite3.connect('gcCatalog.sqlite')
    try:
        c = conn.cursor()

        try:
            c.execute("select barcode from items where barcode = ?", (barcode,))

            row= c.fetchone()
            if row:
                barcode= row[0]
                print(barcode)

            else:
                barcode= None
            if barcode == None:
                not_found()
                barcode= input("Scan the firt barcode: ")
                barcode_check(barcode)

            else:
                print("Good barcode")
                

        finally:
            c.close()

    finally:
        conn.close()

def not_found():
    os.system("aplay shelfReaderSounds/notFound.wav")
    print ('Barcode not found in database.')
    


main()
