#***********************************
#*
#* Document: change directory to target directory (must be static)
#* Author: lightsavers
#* Last update: 05/25/2022
#*
#***********************************

# take and print past and new directory
def changeDirectory(newDirectory):    
    #print current directory
    currentDir = os.getcwd()
    print("Current directory: \n" , currentDir)
   
    #change to specific directory (directory must be static
    path = Path(newDirectory)
    os.chdir(path)
    
    #print new directory
    newDir = os.getcwd()
    print("new directory: \n" , newDir)
    
    print()


#print to console the current directory
if __name__ == "__main__":
    #relevant imports
    import sys
    import os
    from pathlib import Path
    changeDirectory(str(sys.argv[1]))

    