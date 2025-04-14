'''Write a program to count the number of lines, words, and characters in a text file.'''

def count(files):
    try:
        with open(files,'r') as f:
            wcount = 0
            ccount = 0
            lcount = 0

            for line in f:
                lcount +=1
                ccount += len(line)
                words = line.split()
                wcount += len(words)

            print("Output: \n")
            print("The number of lines in the following files are",lcount)
            print("The number of words in the following files are",wcount)
            print("The number of characters in the following files are",ccount)

    except FileNotFoundError:
        print("File not Found!")

files = "program1.txt"
count(files)