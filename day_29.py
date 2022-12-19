# Day 29: Middle Figure

def middle_figure(a,b):
    ab = ''.join(a.split() + b.split())
    if len(ab) % 2 != 0:
        middle = len(ab)//2 
        return ab[middle]
    return "No middle figure"

str1 = "make love"
str2 = "not wars"
print(middle_figure(str1,str2))
