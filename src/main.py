
import subprocess
import pathlib
import os
import json
import numpy

class cleaner(object):
    def __init__(self, *args):
        self.files=[]
        self.path=str(pathlib.Path(__file__).parent.resolve())
        if self.isnotready():
            self.init()
        self.getconfigs()
        
    def getconfigs(self):
        with open(self.path+'/config.json') as configfile:
            configs = json.loads(configfile.read())
        for keywords in configs['keywords']:
            self.files.append(keywords) #list of dict with configs

    def init(self):
        print("création des fichiers...")
        os.system('chmod a+rwx init.sh')
        os.system(self.path+"/init.sh") #crea fichiers necessaires

    def isnotready(self):
        os.system('chmod a+rwx isready.sh')
        return abs((int(subprocess.check_output([self.path + '/isready.sh'])))-1)
        #check existance filecleaner
cleaner = cleaner()
