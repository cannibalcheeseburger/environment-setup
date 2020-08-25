from . import constants

def main():
    # Making Readme.md
    print("===================Creating Readme=====================\n")


    with open("README.md",'w') as R:
        R.writelines(constants.Readme)

    print("===================Created Readme======================\n\n\n")


    ## Creating License

    print("===================Creating License=====================\n")

    with open("LICENSE",'w') as L:
        L.writelines(constants.license)

    print("===================Created License======================\n\n\n")


    ## Making gitignore

    print("===================Creating gitignore=====================\n")

    with open(".gitignore",'w') as git:
        git.writelines(constants.gitignore)

    print("===================Created gitignore======================\n\n\n")


    # Manifest

    print("===================Created MANIFEST.in======================\n\n\n")

    with open("MANIFEST.in",'w') as M:
        M.writelines(constants.manifest)

    print("===================Created MANIFEST.in======================\n\n\n")


if __name__ == "__main__":
    main()