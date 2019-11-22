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

def FindWordCount(filename,word):
    count=0
    for i in range(len(filename)):
        for j in filename[i].split():
            if j == word:
                count=count+1
    return count

def ScoreFinder(listofplayers, listofscores, name):
    fixedname = name.capitalize()
    if fixedname not in listofplayers:
        PrintOutput(f'player not found')
        return
    place = listofplayers.index(fixedname)
    score = listofscores[place]
    PrintOutput(f'{listofplayers[place]} got a score of {score}')

def Union(list1,list2):
    finallist = list1 + list2
    return list(dict.fromkeys(finallist))

def Intersection(list1,list2):
    bothlist = []
    for i in list1:
        if i in list2:
            bothlist.append(i)
    return bothlist

def NotIn(list2,list1):
    notinlist = []
    for i in list2:
        if i not in list1:
            notinlist.append(i)
    return notinlist
