import os
import hashlib
import sqlite3
from rich.table import Table
from rich.console import Console

conn = sqlite3.connect('filehashdb.sqlite3')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS filehash")
c.execute("""CREATE TABLE filehash (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
                                    filename TEXT UNIQUE, 
                                    filehash TEXT)""")

# prompt the user for *path*, try again until the user gives a correct path
def getPath():
    try:
        while True:
            path = input('Enter the specific path to the desired directory: ')
            if os.path.isdir(path):
                return path
            else:
                print('Please enter a valid path')
    except Exception as exc:
        print(f'{exc} error has occured, try again!')
        getPath()


def hashFiles(path):
    # get old working directory
    owd = os.getcwd()
    # for each item found, create a new path with it
    # check if the new path is a directory path
    # if True, perform a recursion until False
    for name in os.listdir(path):
        # path --> ../folder_x OR ../folder_x/file_x.txt
        newPath = os.path.join(path, name)
        if os.path.isdir(newPath):
            hashFiles(newPath)
        else:
            # change the working directory to the new path created above
            # ../folder_x/file_x.txt
            os.chdir(path)
            # open the item --> read file --> hash the content
            with open(name, 'rb') as file:
                fileData = file.read()
                fileHash = hashlib.md5(fileData)
                hashValue = fileHash.hexdigest()
            # open a cursor
            # insert the name and hashValue into the data base
            # if the name already exists, update it
            c = conn.cursor()
            c.execute('INSERT OR REPLACE INTO filehash (filename, filehash) VALUES (?,?)', (name ,hashValue))
            conn.commit()
            # switch back to the old working directory
            os.chdir(owd)
            # close cursor
            c.close()


def printFile():
    c = conn.cursor()
    c.execute('SELECT filename, filehash FROM filehash ORDER BY filename')
    rows = c.fetchall()
    # if fetchall returns an empty list then print "there is no file in the database"
    if len(rows) == 0:
        print("""
------------------------------------------
There is no file in the database
------------------------------------------""")
    # else print results
    else:
        console = Console()
        table = Table(show_header=True, show_lines=True, header_style="bold magenta")
        table.add_column("File Name", style="bold")
        table.add_column("File Hash")

        for row in rows:
            table.add_row(
                f"{row[0]}",
                f"{row[1]}"
            )
        console.print(table)
    c.close()

## Main #####################
destination_path = getPath()

hashFiles(destination_path)
printFile()