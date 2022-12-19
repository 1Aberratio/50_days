# Most Repeated Name

def repeated_name(nlist):
    names = [(nlist.count(name),name) for name in set(nlist)]
    repeated = sorted(names)
    return repeated[-1][1]
    
name = ['John', 'Peter', 'John', 'Peter', 'Jones', 'Peter']
print(repeated_name(name))

print('-'*35)

# Extra Challenge: Sort by Last Name

def sorted_names(sNames):
    midName = [' '.join(nm.split()[::-1]) for nm in sNames]
    return sorted(midName)

schoolList = ["Beyonce Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise"]
schoolList2 = ["Janis Joplin", "Jimi Hendrix", "Aretha Franklin", "Jack White", "Tilda Swinton"]
print(sorted_names(schoolList))
print(sorted_names(schoolList2))
