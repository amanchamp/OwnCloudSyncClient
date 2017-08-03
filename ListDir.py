import os 

def getPath():
    path = '/Users/amandeep/TestDir'
    return path;

def getFiles():
    path = getPath()
    fileList = [ ]
    for path, dirs, files in os.walk(path):
        fileList.append(path)
        for f in files:
            if not f[0] == '.':
                fileList.append(f)
    return fileList;

