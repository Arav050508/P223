import zipfile
import time

folderpath = input("Path to the file: ")
zipf = zipfile.ZipFile(folderpath)

if not zipf:
    print("The zipped folder/file is not passowrd protected!")
else:
    starttime = time.time()
    result = 0
    c = 0

    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   

    file_open = open("wordlist.txt", "w")

    for i in characters:
        for j in characters:
            for k in characters:
                for l in characters:
                    guess = str(i) + str(j) + str(k) + str(l)

                    file_open.write(guess)
                    file_open.write('\n')

                    c += 1
    
    print("Wordlist of {} passwords created!".format(c))