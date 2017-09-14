import random

f = open('occupations.csv','r')

str = f.read()
li = str.split('\n')
#print li
#print len(li)
linested = []
for element in li:
    linested.append(element.split(','))
#print linested
linested.remove(linested[len(linested)-1])

index1 = 0
while index1 < len(linested):
    current = linested[index1]
    print current[0]
    if current[0][0] == '"':
        while len(current) > 2:
            current[0] = current[0].replace('"','') + ',' + current[1].replace('"','')
            current.remove(current[1])
    index1 += 1

print linested



    
        


'''
index = 1
dic = {}
while index < len(liheader):
    
    index += 1
'''
