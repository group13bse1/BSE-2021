fileHandle = open('measles.txt')
lowest = None
highest = None
for line in fileHandle:
    year = line[-5:]
    year= year.strip()
    #print(year)

    if (lowest is None) or (highest is None):
        lowest = year
        highest = year
    elif lowest >year :
        lowest = year
    elif highest < year:
        highest = year

print(highest)
print(lowest)
