import zipfile
import time

folderpath = input("Path to the file: ")
zipf = zipfile.ZipFile(folderpath)

global result
global tried

result = 0
tried = 0
c = 0

if not zipf:
    print("The zipped folder/file is not password protected!")
else:
    starttime = time.time()
    wordListFile = open("wordlist.txt", "r", errors = "ignore")
    body = wordListFile.read().lower()
    words = body.split("\n")

    for i in range(len(words)):
        word = words[i]
        password = word.encode("utf8")
        c += 1

        print("Trying to decode password by: {}".format(word))

        try:
            with zipfile.Zipfile(folderpath, "r") as zf:
                zf.extractall(pwd = password)

                print("Success! The password is: " + word)
                endtime = time.time()
                result = 1
            break
        except:
            pass
    
    duration = endtime = starttime

    if result == 0:
        print("Sorry, password was not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of four characters.")
    else:
        print("Congratulations! Password found after trying "+str(c)+" combinations in "+str(duration)+" seconds.")