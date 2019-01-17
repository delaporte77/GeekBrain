import os
import shutil
import glob

def copyFiles():

    for files in glob.iglob('./test/**/*.*', recursive=True):
        shutil.copy(files, './test')

def deleteFolders():

    for i in os.listdir('./test'):
        if os.path.isdir('./test/{0}'.format(i)):
            shutil.rmtree('./test/{0}'.format(i))

copyFiles()
deleteFolders()
