import os.path
import sqlite3
import ListDir as fl


def init():
    if os.path.exists('fileList.db'):
      print 'Table Exists'
    else:
        print 'Creating Table ...'
        con = sqlite3.connect('fileList.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE Files(FileName TEXT, Directory TEXT, Size INT) ")
        con.commit()
        print 'Done Creating Table'
    return

 def storeFileInfo(fileArray):
    for f in fileArray:
        if f[0]== 








checkTable()