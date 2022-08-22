import collections
#used to extract goals of each team
def getnums(string):
    emp_str = ""
    for m in string:
        if m.isdigit():
            emp_str = emp_str + m
    return emp_str
#used to extract the name of each team in a match
def getname(string):
    emp_str = ""
    for m in string:
        if not m.isdigit():
            emp_str = emp_str + m

    return emp_str.strip()
#used to get all team names from file
def getAllnames(lines):
    teams = []
    teamnames = []
    for line in lines:
        splitted = line.split(',')
        for team in splitted :
            teams.append(team)
    for teamname in teams :
        result = ''.join([i for i in teamname if not i.isdigit()])
        teamnames.append(result.strip())
    return set(teamnames)
ff = input('Please enter the matches txt file : ')
f = open(ff,'r')
teampoints = {}
readfile = f.read().splitlines()
#saves teams as dictionary
for team in getAllnames(readfile) :
    teampoints.update({team : '0'})
#checking score for each line and giving points to each team depending on the match score
for line in readfile :
    line = line.split(',')
    a = getnums(str(line[0]))
    b = getnums(str(line[1]))
    team1 = getname(line[0])
    team2 = getname(line[1])
    if int(a) == int(b) :
        teampoints.update({team1: str(int(teampoints[team1])+1)})
        teampoints.update({team2: str(int(teampoints[team2]) + 1)})
    elif int(a) > int(b):
        teampoints.update({team1: str(int(teampoints[team1]) + 3)})
    elif int(b) > int(a):
        teampoints.update({team2: str(int(teampoints[team2]) + 3)})
#creating multiple dictionaries for appending , editing , and other things
arrangedDict = {k: v for k, v in sorted(teampoints.items(), key=lambda item: item[1],reverse=True)}
newDict = {k: v for k, v in sorted(teampoints.items(), key=lambda item: item[1],reverse=True)}
duplicates = ([item for item, count in collections.Counter(arrangedDict.values()).items() if count > 1])
#arranging duplicates in alphabetic mode
for i in duplicates :
    duplicated = {}
    for item in arrangedDict :
        if i in arrangedDict[item]:
            duplicated.update({item:str(i)})
            newDict.pop(item)
    items = list(newDict.items())
    for dup in reversed(sorted(duplicated)) :

        rang =list(arrangedDict.values()).index(i)
        items.insert(rang,(dup,arrangedDict[dup]))
    mydict = dict(items)
#printing as the given form
for item in mydict :
    if teampoints[item] == '1':
        print(f'{item} , {mydict[item]} pt')
    else:
        print(f'{item} , {mydict[item]} pts')






