# File to compile all possible projects in specified folders
# Directory structure assumed to be
# | <folder>/build/<app>/gcc/bin/
# 
# <folder> list is specified here. 
# <app> will be determined from <folder> list
import os
import subprocess

# Class: 
#   <folder>
#   <app>
#   <binary output>
class Project:
    def __init__(self, folder, app):
        self.folder = folder
        self.app = app
        self.makeCommand = f'make -C {self.folder}/build/{self.app}/gcc'
        self.binaryOutput = f'{self.folder}/build/{self.app}/gcc/bin/{self.app}.elf'

    #def get_Folder(self):


# This function returns the list to compile from the specified folder
def generateCompileList(folder):
    # Get current working directory.  This file should be root/build.
    search_path = os.path.abspath(os.path.join('..', folder, 'build'))

    dir_list = [filename for filename in os.listdir(os.path.join(search_path)) if os.path.isdir(os.path.join(search_path, filename))]
    dir_list_string = ','.join(dir_list)
    print(f'generateCompileList ({search_path}): {dir_list_string}')

    # remove "common" folder which should not be compiled directly


# This function executes commands 
def executeCommand(command):
    build_command = ' '.join(command)
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(result.stdout)
        print(f"Build ({build_command}) successful")
        return(0)
    except subprocess.CalledProcessError as e:
        print("Build ({build_command}) was terminated by signal: {e.returncode}")
        print(e.output)
        return(e.returncode)
    except OSError as e:
        print(f"Build ({build_command}) failed:  {e.returncode}")
        return(-1)




def main():
    # List all sub-folders in specified <folder>
    to_compile_folders = ['ble-apps',
                          'ble-mesh-apps',
                          'controller']
    
    for folder in to_compile_folders:
        compile_list = generateCompileList(folder)

    # Combine all sub-folders 
   

if __name__ == "__main__":
    main()