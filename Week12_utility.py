#   Incremental Build Model
#   Tayler Jone
#  ​ CSCI 102 – Section A
#   Week 12 - Part A

def PrintOutput(a):
    print('OUTPUT', a)

def LoadFile(filename):
    List = []
    sublist = []
    file = open(filename, 'r')
    List = (file.readlines())
    for i in List:
        sublist.append(i[0:-1])
    return sublist

def UpdateString(string,new,location):
    newstring = ''
    for i in range(len(string
                       )):
        if i == location:
            newstring += new
        else:
            newstring += string[i]
    PrintOutput(newstring)
