import subprocess
def clear_console()->None:
    subprocess.run('clear', shell=True)
#install dependecies
dependencies = ['cmake', 'qt', 'libarchive', 'sqlite', 'wget', 'unzip']
for package in dependencies:
    result = subprocess.run(['brew', 'install', package],capture_output=True ,text=True)
    print(result)



wget_result = subprocess.run(['wget', 'https://github.com/zealdocs/zeal/archive/refs/tags/v0.7.2.zip'], capture_output=True, text=True) #install source code zip
print(wget_result)
unzip_result = subprocess.run(['unzip', 'v0.7.2.zip'], capture_output=True, text=True) #unzip. I hard coded it because I could not figure out how to not so I included if statment in case it doesn't work
print(unzip_result)
if unzip_result.returncode == 1:
    clear_console()
    print("run the unzip command followed by the zip file that should be something like v0.7.2.zip")
else:
    clear_console()
    print("cd to the new directory created from unzipping the file(somehing like zeal-0.7.2/)")
    print("""run the commands 
                             cmake -B build
                             cmake --build build""")
