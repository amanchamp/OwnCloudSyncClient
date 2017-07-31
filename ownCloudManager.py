import owncloud
import time
import ownCloudAuth as auth
def login():
    oc = auth.login()
    return oc
def createDir(folderName):
    oc = login()
    oc.mkdir(folderName)
def uploadFile():
    oc = login()
    oc.put_file('testDir/level1.txt', '/Users/amandeep/TestDir/level1.txt')


createDir('testDir')
time.sleep(2)
uploadFile()