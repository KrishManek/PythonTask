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

print(f"mark {marks}")
avgmarks={marks[name]/persubavgmarks[name] for name in marks}
print(f"Average Marks: {avgmarks}")

print(f"Subject Wise: {subjectwise}")

# Highest marks
res = max(marks,key=lambda i: marks[i])
print(f"Highest Score Name: {res} Score : {marks[res]}")

#Subject-Wise highest marks 



#sort function 
sort = sorted(marks.items(), key=lambda x: x[1], reverse=True)
print(f"Sort: {sort}")

