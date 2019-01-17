import os
import shutil

def createFolders():

    for i in range(1, 9):
        os.mkdir('./dir_{0}'.format(i))

def removeFolders():

    for i in os.listdir('.'):
        if 'dir' in i:
            shutil.rmtree('./{0}'.format(i))

createFolders()
removeFolders()