# Exercise 6: Rewrite the program that prompts the user for a list of numbers and 
# prints out the maximum and minimum of the numbers at the end when the user 
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum numbers
# after the loop completes.

numberlist = []
while(True):
    number_str = input("\nEnter any number of numbers and type done at the end: ")
    number_str = number_str.strip()
    number_str = number_str.lower()
    if number_str == "done":        
        break
    number_str_list = number_str.split()
    print(number_str_list)
    for str_number in number_str_list:
        number = float(str_number)
        numberlist.append(number)

if len(numberlist) > 0:
    print("\nMax number from the given list : ",max(numberlist))
    print("\nMin number from the given list : ",min(numberlist))
    print("\nCount number from the given list : ",len(numberlist))
    print("\nAverage of the given number : ", sum(numberlist)/len(numberlist))

