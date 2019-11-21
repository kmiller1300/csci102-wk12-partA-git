#Katelyn Miller
#CSCI 102- C
#Week 12 Part A
def PrintOutput(s):
    return print("OUTPUT",s)
def LoadFile(name):
    file=open('name.txt','r')
    lines=file.readlines()
    
    return lines
print('\n')
def UpdateString(s1, s2, n):
    newstring=s1[0:n]+s2+s1[n+1: len(s1)]
    
    
    return newstring
def FindWordCount(l, s):
    count=0
    for i in l:
        if i==s:
            count+=1
    return count

def ScoreFinder(players, scores, s):
    if s not in players:
        print("Player not found")
    if s in players:
        i=players.index(s)
        print(s,"got a score of",scores[i])

def Union(list1, list2):
    finalList=[]
    for i in list1:
        finalList.append(i)
    for j in list2:
        finalList.append(i)
    print(finalList)

def Intersection(list1, list2):
    newList=[]
    for i in list1:
        if i in list2:
            newList.append(i)
    print(newList)
        
            
