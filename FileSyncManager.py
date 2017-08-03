import ListDir as fl
import ownCloudManager as manager


def removeEmpty(array):
    parsed = []
    for a in array:
        if not a == '':
            parsed.append(a)
    return parsed;



def getTopLevel(f):
    split = removeEmpty(f.split('/'))
  
    return  split[len(split)-1];

        

files = fl.getFiles()
print 'Files'
print files
directoryOwnCloud = ' '
directoryLocal = ' '


for f in files:
    if f[0] == '/':
        directoryLocal = f
        directoryOwnCloud +=getTopLevel(f) + '/'
        print 'LOCAL DIRECTORY:   ' + directoryLocal
        manager.createDir(directoryOwnCloud)
    elif not f[0] == '/':
        print 'File Upload Local:  ' + directoryLocal + '/' + f
        print 'File Upload Remote:  ' + directoryOwnCloud  + f
        manager.uploadFile(directoryOwnCloud  + f, directoryLocal + '/' + f)

print directoryOwnCloud



