"""Exercise 1: Write a function called chop that takes a list 
and modifies it,removing the first and last elements, 
and returns None. 
Then write a function called middle that takes a list and 
returns a new list that contains all but the first and last 
elements."""

# def chop(t):
#     t[:] = t[1:-1]
    
# list1 = ['a','b','c','d','e']
# print("\nOrignal list :",list1)
# chop(list1)
# print("\n",list1)
# chop(list1)
# print("\n",list1)

# def middle(m):
#     newm = m[1:-1]
#     return newm

# list2 = ['a','b','c','d','e','f','g','h']
# print("Before calling middle : ", list2)
# newmiddle = middle(list2)
# print("After calling middle :",newmiddle)

# print("Before calling middle : ", newmiddle)
# newmiddle = middle(newmiddle)
# print("After calling middle :",newmiddle)

# deepa coding

l2 = []
def chop(ls):
    f = ls.pop(0)
    l = ls.pop()
    l2.append(f)
    l2.append(l)
    return ls
    
l1 = [1,2,3,4]
chop(l1)

# # how to change string to list
# s = 'spam-spam-spam'
# # delimiter = '-'
# u= s.split('-')
# print(u)


# # how to change list to string
# msg = ['I ',' love ',' you ',' mohana ']
# v = '$$$'.join(msg)
# print(v)
# msg = ['I','love','you','mohana']
# v = ' '.join(msg)
# print(v)
