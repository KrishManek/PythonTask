mydict = {
    'nilesh-geography': 89,
    'alpesh-history': 77,
    'shital-math': 93,
    'dimpal-hindi': 68,
    'nilesh-english': 74,
    'alpesh-sci': 85,
    'shital-history': 91,
    'dimpal-geography': 87,
    'nilesh-sci': 83,
    'alpesh-math': 92,
    'dimpal-english': 78,
    'shital-hindi': 81,
    'nilesh-history': 90,
    'alpesh-geography': 79,
    'dimpal-math': 84,
    'shital-sci': 88,
    'nilesh-hindi': 71,
    'alpesh-english': 80,
    'dimpal-sci': 89,
    'shital-geography': 82,
    'nilesh-math': 93,
    'alpesh-hindi': 75,
    'dimpal-history': 90,
    'shital-english': 87
}
marks={}
persubavgmarks ={}
subjectwise = {}
count = 0
avgmarks={}
for namesub, mark in mydict.items():
    name = namesub.split("-")[0]
    sub = namesub.split("-")[1]
    if marks.get(name):
        marks[name] += mark
    else:
        marks[name] = mark
    # persubavgmarks
    if persubavgmarks.get(name):
        persubavgmarks[name] += 1
    else:
        persubavgmarks[name] = 1
        
	#Subjectwise Highest marks 
    if subjectwise.get(sub):
        subjectwise[sub] = mark if mark > subjectwise[sub] else subjectwise[sub]
    else:
        subjectwise[sub] = mark

print(f"\n 1) Printing Total Marks of each students: {marks} \n")

avgmarks={name : round(marks[name]/persubavgmarks[name],2) for name in marks} #creating a new dict to caluclate & store average marks of each student
print(f"\n 2) Average marks scored by individual students: {avgmarks} \n")

print(f"\n 3) Subject Wise Highest Marks scored: {subjectwise} \n")

# Highest marks
res = max(marks,key=lambda i: marks[i]) #calculating highest total score 
print(f"\n 4) Highest Total Score secured by Name: {res} Score : {marks[res]} \n")

#sort function 
sort = dict(sorted(marks.items(), key=lambda x: x[1], reverse=True)) #using Sorted function to sort values #reverse = True for descending order
print(f"\n 5) Sorting Values in Descending Order: {sort} \n")

