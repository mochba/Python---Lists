# Exercise: the program to compute an average without a list:

# value =  0.0
# count = 0
# while True:
#     inp = input("Enter numbers and done")
#     inp = inp.lower()
#     if inp == 'done':
#         break
#     else:
#         float_number = float(inp)
#         print(float_number)
#         value =  value + float_number
#         count = count + 1
# print(value ,count,value/count)

# Exercise: Now the program to compute an average with a list:

# number_list = list()
# value = 0.0
# count = 0
# while True:
#     inp_num = input("Enter a number : ")
#     inp_num = inp_num.lower()
#     if inp_num == 'done':
#         break
#     else:
#         inp_num = float(inp_num)
#         number_list.append(inp_num)
# value =  sum(number_list)/len(number_list)
# print("List of the enter number is :",number_list)
# print("Average of the entered numbers is : ",value)

# Running sum

from itertools import accumulate
number_list = list()
while True:
    inp_num = input("Enter a number : ")
    inp_num = inp_num.lower()
    if inp_num == 'done':
        break
    else:
        inp_num = float(inp_num)
        number_list.append(inp_num)
print(list(accumulate(number_list)))

