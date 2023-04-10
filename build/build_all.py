# File to compile all possible projects in specified folders
# Directory structure assumed to be
# | <folder>/build/<app>/gcc/bin/

import os
import subprocess

# Class: 
#   <folder>
#   <app>
#   <binary output>
class Project:
    def __init__(self, folder, app):
        self.folder = os.path.join(folder, 'build', app)
        self.app = app
        self.makeCommand = ['make', '-C ', os.path.join(self.folder, 'gcc')]
        self.binaryOutput = os.path.join(self.folder, 'gcc', 'bin', self.app + '.elf')
        self.buildResult = None

    def printInfo(self):
        print(f'{self.folder}:')
        print( '    build: '+ ' '.join(self.makeCommand))
        print(f'    binary: {self.binaryOutput}')



# This function returns the list to compile from the specified folder
def generateCompileList(folder):
    # Get current working directory.  This file should be root/build.
    search_path = os.path.join(os.path.abspath(folder), 'build')

    dir_list = [filename for filename in os.listdir(os.path.join(search_path)) if os.path.isdir(os.path.join(search_path, filename))]
    dir_list_string = ','.join(dir_list)
    print(f'generateCompileList ({search_path}): {dir_list_string}')

    # remove "common" folder which should not be compiled directly
    remove_dir_list = ['common']
    dir_list = [foldername for foldername in dir_list if foldername not in remove_dir_list]
    
    return dir_list


# This function executes commands 
def executeCommand(command):
    build_command = ' '.join(command)
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(result.stdout)
        print(f"Build ({build_command}) successful")
        return("Success")
    except subprocess.CalledProcessError as e:
        print(f"Build ({build_command}) was terminated by signal: {e.returncode}")
        print(e.output)
        return(f"Failed {e.returncode}")
    except OSError as e:
        print(f"Build ({build_command}) failed:  {e.returncode}")
        return("Error")




def main():
    projects_to_compile = []

    print(os.path.abspath())

    # List all sub-folders in specified <folder>
    to_compile_folders = ['ble-apps',
                          'ble-mesh-apps',
                          'controller']
    
    for folder in to_compile_folders:
        compile_list = generateCompileList(folder)
        for app in compile_list:
            projects_to_compile.append(Project(folder, app))

    # Print all images
    for app in projects_to_compile:
        app.printInfo()
        app.buildResult = executeCommand(app.makeCommand)
        print (f'{app.app} compile {app.buildResult}')
   

if __name__ == "__main__":
    main()