import os 

def getPath():
    path = '/Users/amandeep/TestDir/'
    return path;


def listDir(path):
    for path, dirs, files in os.walk(path):
        print path
        for f in files:
            print f
    return;

path = getPath()
listDir(path)