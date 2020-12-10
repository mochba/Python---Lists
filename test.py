'''Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt. Write a 
program to open the file romeo.txt and read it line by line. For each line, split
the line into a list of words using the split function. For each word, check to 
see if the word is already in a list. If the word is not in the list, add it to 
the list. When the program completes, sort and print the resulting words in
alphabetical order.'''

# /home/appu/Documents/python_workbench/Chuks_python/List/romeo.txt
# wordlist = []
# try:
#     stream = open(input("Enter :"))
#     for eachline in stream:
#         words = eachline.split()
#         for word in words:
#             word = word.lower()
#             if word not in wordlist:
#                 wordlist.append(word)
#     wordlist.sort()
#     print(wordlist)

# except:
#     print("File not found")
#     quit()

"""Exercise 5 :Write a program to read through the mail box data and when you find line that 
starts with “From”, you will split the line into words using the split function.
We are interested in who sent the message, which is the second word on the From 
line."""
# # /home/appu/Documents/python_workbench/Chuks_python/List/mbox-short.txt
# emaillist = list()
# try:
#     stream = open(input("Enter"))
#     for eachline in stream:
#         # print(eachline)
#         if eachline.startswith("From"):
#             linelist = eachline.split()
#             if linelist[1] not in emaillist:
#                 emaillist.append(linelist[1])
#     print("\n",emaillist,"\n")
# except:
#     print("Enter a valid file name")
#     quit()

"""Exercise 6: Rewrite the program that prompts the user for a list of numbers and 
# prints out the maximum and minimum of the numbers at the end when the user 
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum numbers
# after the loop completes."""
num_list = []
while True:
    number_str = input("Enter number :")
    number_str = number_str.lower()
    if number_str == "done":
        break

    numb = number_str
    print(int(numb))
    if numb not in num_list:
        print(number_str)
    # #     num_list.append(number_str)
    # # print(num_list)