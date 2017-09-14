import random

#Opens file
f = open('occupations.csv','r')

#Reads and closes file
str = f.read()
f.close()

#Creates list of file lines
li = str.split('\n')
linested = []


#Creates nested list of file lines and their commas
for element in li:
    linested.append(element.split(','))
linested.remove(linested[len(linested)-1])

normal_val = len(linested[0])

#Parses through linested and takes care of any falsely spliced commas that are in between quotes
index1 = 0
while index1 < len(linested):
    current = linested[index1]
    if current[0][0] == '"':
        while len(current) > normal_val:
            current[0] = current[0].replace('"','') + ',' + current[1].replace('"','')
            current.remove(current[1])
    index1 += 1


#Creates "header" to initialize dictionary building
liheader = linested[0]
linested.remove(linested[0])
#print liheader
#print linested



#Builds dictionary!
DATA = {}
for sublist in linested:
    lookup = {}
    index = 1
    while index < len(liheader):
        lookup[liheader[index]]=sublist[index]
        index += 1
        DATA[sublist[0]] = lookup
        

print DATA
    


