'''Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt. Write a 
program to open the file romeo.txt and read it line by line. For each line, split
the line into a list of words using the split function. For each word, check to 
see if the word is already in a list. If the word is not in the list, add it to 
the list. When the program completes, sort and print the resulting words in
alphabetical order.'''

# /home/appu/Documents/python_workbench/Chuks_python/List/romeo.txt
wordlist = list()
filename = input("Enter a file name:")

try:
    stream = open(filename)
    for eachline in stream:
        # eachline = eachline.lstrip()
        eachline = eachline.split()
        for i in eachline:
            i = i.lower()
            if i not in wordlist:
                wordlist.append(i)       
        wordlist.sort()    
    print("\n",wordlist,"\n")
except:
    print("File not found")
    quit()

