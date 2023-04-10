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
        self.name = f'{folder}-{app}'
        self.folder = os.path.join(folder, 'build', app)
        self.makeCommand = ['make', '-C', os.path.join(self.folder, 'gcc')]
        self.binaryOutput = os.path.join(self.folder, 'gcc', 'bin', app + '.elf')
        self.buildResult = None

    def printInfo(self):
        print(f'{self.folder}:')
        print( '    build: '+ ' '.join(self.makeCommand))
        print(f'    binary: {self.binaryOutput}')
        print(f'    buildResult: {self.buildResult}')



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
        print("------- Build Log ----------")
        print(result)
        print("----------------------------")
        print(f"Build ({build_command}) successful")
        return("Success")
    except subprocess.CalledProcessError as e:
        print(f"Build ({build_command}) was terminated by signal: {e.returncode}")
        print(e.output)
        return(f"Failed {e.returncode}")
    except OSError as e:
        print(f"Build ({build_command}) failed:  {e.returncode}")
        print(e.output)
        return("Error")




def main():
    projects_to_compile = []

    print(os.path.abspath('.'))

    # List all sub-folders in specified <folder>
    to_compile_folders = ['ble-apps',
                          'ble-mesh-apps',
                          'controller']
    
    for folder in to_compile_folders:
        compile_list = generateCompileList(folder)
        for app in compile_list:
            projects_to_compile.append(Project(folder, app))

    # Compile all images
    for app in projects_to_compile:
        app.printInfo()
        app.buildResult = executeCommand(app.makeCommand)
        print (f'{app.name} compile {app.buildResult}')

    # Check each image to determine if there were any failures
    # Keep a list of successful images and failed image
    successful_compile = [app.name for app in projects_to_compile if 'Success' in app.buildResult]
    failed_compile = [app.name for app in projects_to_compile if 'Failed' in app.buildResult]
    didnt_compile = [app.name for app in projects_to_compile if not app.buildResult]

    print('Successful Compilation: ' + ','.join(successful_compile))
    print('Failed Compilation: ' + ','.join(failed_compile))
    print('Compilation Not Executed: ' + ','.join(didnt_compile))

if __name__ == "__main__":
    main()