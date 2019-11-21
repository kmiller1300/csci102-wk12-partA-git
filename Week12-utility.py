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
    newstring=''
    i=0
    for s1[i] in s1:
        if i==n:
            newstring[i]=s2[i]
        elif i!=n:
            newstring[i]=s1[i]
    return newstring

        
