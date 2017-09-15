import random

#Opens file
f = open('occupations.csv','r')

#Reads and closes file
str = f.read()
f.close()

#Creates list of file lines
li = str.replace('\r',"").split('\n')
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
        try:
            lookup[liheader[index]]=float(sublist[index])
        except Exception as e:
            lookup[liheader[index]]=sublist[index]
        index += 1
        DATA[sublist[0]] = lookup
        
print 'This is the dictionary!'
print DATA


#Random selection
def random_job():
    random_selection = random.uniform(0,99.8)
    #print random_selection
    where_i_am = 0.0
    for key in DATA:
        where_i_am += DATA[key]['Percentage']
        #print where_i_am
        if(where_i_am >= random_selection):
            return key
            break

    
#Run tests, output is a dictionary with the difference in listed percentages and test percentages.
#As close as possible to zero is optimal.
i = 0
test_dic = {}
for key in DATA:
    test_dic[key] = 0.0

runthismanytimes = 1000000
while(i < runthismanytimes):
    selected = random_job()
    test_dic[selected] = test_dic[selected] + 1
    i+=1

for key in test_dic:
    test_dic[key] = DATA[key]['Percentage'] - (test_dic[key]/runthismanytimes)*100

print 'These are the test cases! As close to zero is good! Means test data was very close to listed percentages'
print test_dic
'''
print random_job()
'''

