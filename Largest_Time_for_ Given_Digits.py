# Largest Time for Given Digits

l = [1,7,5,7]





def printme(l):
    s=""
    for i in range(2):
        s= s + str(l[i])
    s = s + ":"
    print(s)
    for j in range(2,4):
        s = s + str(l[j])
    print(s)
    return s


printme(l)