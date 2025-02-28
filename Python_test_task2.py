"""
numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]
# this list may have N number of element
Expected output:
Duplicate Numbers and Their Counts:
4 appears 3 times
5 appears 2 times
6 appears 2 times
7 appears 2 times
"""
countduplicateno = {}
numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]
def countduplicate(number):
    for no in numbers:
        if no in countduplicateno:
            countduplicateno[no] += 1
        else:
            countduplicateno[no] = 1
    printduplicateval(countduplicateno)

def printduplicateval(countduplicateno):
    print("Duplicate Numbers and Their Counts:")
    for key, value in countduplicateno.items():
        if value == 1:
            pass
        else:
            print(f"{key} appears {value} times")

countduplicate(numbers)