# Write a small program that read a .txt file and looks for lines that starts with 
# “From”, split those lines, and then print out the third word in the line:
# print out the day of the week from those lines that start with “From”
# 'mbox-short.txt'

# Documents/python_workbench/home/appu/Documents/python_workbench/mbox-short.txt

filename = input("enter a file name :")

try:
    stream = open(filename)
    for eachline in stream:
        eachline.strip()
        if eachline.startswith("From "):
            # print(eachline)
            eachline = eachline.split()
            # print(eachline)
            print(eachline[2])
except:
    print("File not found")
    quit()