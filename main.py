import constants
import os 
import sys


#os.chdir(path+sys.argv[1])
name = "sample"

def clone_repo():
    print("===Cloning git Repository===\n")
    url = "https://github.com/cannibalcheeseburger/environment-setup.git"
    os.system("git clone "+ url)
    #change directory to git repo
    #os.chdir()

def create_pipenv():
    print("creating virtual environment")
    os.system("pipenv install")
    os.system("pipenv shell")

def make_dir():
    os.mkdir(name)
    with open(name+'/__init__.py', 'w') as fp: 
        pass
    with open(name+'/__main__.py', 'w') as fp: 
        pass
    os.mkdir("tests")
    with open('tests/__init__.py', 'w') as fp: 
        pass

def main():
 #   if len(sys.argv)<2:
  #      print("cant")
   #     return
    path = "."
    
    path_if = "D:/GITHUB/MERE_WALE/"
    global name 
    name = input("Enter name of project:")
    if path_if!="":
        path = path_if
    os.mkdir(path+name)
    os.chdir(path+name)
    #clone_repo()
    imp_files()
    #make_dir()
    create_pipenv()



def imp_files():
    # Making Readme.md
    print("Creating README.md")
    with open("README.md",'w') as R:
        R.writelines(constants.Readme.format(name=name))
    
    ## Creating License
    print("Creating LICENSE")
    with open("LICENSE",'w') as L:
        L.writelines(constants.license)
    
    ## Making gitignore
    print("Creating gitignore")
    with open(".gitignore",'w') as git:
        git.writelines(constants.gitignore)
    
    # Manifest
    #print("Creating MANIFEST.in")
    #with open("MANIFEST.in",'w') as M:
    #    M.writelines(constants.manifest)
    
     # Setup
    #print("Creating Setup.py")
    #with open("setup.py",'w') as S:
    #    S.writelines(constants.setup)
    
if __name__ == "__main__":
    main()