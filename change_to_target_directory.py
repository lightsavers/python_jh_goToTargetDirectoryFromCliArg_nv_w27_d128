'''***********************************
*
* Document: change directory to target directory within script
* Author: lightsavers
* Last update: 05/25/2022
*
***********************************'''
#relevant imports
import sys
import os
from pathlib import Path


# take and print past and new directory
class directoryFileOperation(object):
    def changeDirectory(self, newDirectory):    
        
        #print current directory
        currentDir = os.getcwd()
        print("Current directory: \n" , currentDir)
    
        #change to specific directory (directory must be static
        path = Path(newDirectory)
        os.chdir(path)
        
        #print new directory
        self.newDir = os.getcwd()
        print("new directory: \n" , self.newDir)
        
        print()


#print to console the current directory
if __name__ == "__main__":
    fsoper = directoryFileOperation()
    fsoper.changeDirectory(str(sys.argv[1]))

    