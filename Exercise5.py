"""Exercise 5 :Write a program to read through the mail box data and when you find line that 
starts with “From”, you will split the line into words using the split function.
We are interested in who sent the message, which is the second word on the From 
line."""
emaillist = []
filename = input("Enter a file name :")

try:
    stream =  open(filename)
    for eachline in stream:
        if eachline.startswith("From "):
            eachline = eachline.strip()
            eachline = eachline.split()
            emaillist.append(eachline[1])
    print("\n",emaillist)
    print("\nTotal number of emails in the text file are :",len(emaillist),"\n")
except:
    print("File not found")
    quit()

