# Day 14 : Flatten the List

def flat_list(theList):
    return sum(theList, [])
    # Also you can use numpy:
    # Option 1 => return map(flatten, theList) 
    # Option 2 => return np.flatten(theList)

nested_list = [[2,4,5,6]]
# nested_list = [[2,4,5,6], [7,8,9,0]]
print(flat_list(nested_list))

print('-'*35)

# Extra Challenge: Teacher’s Salary

def your_salary():
    teacher = input("Enter the teacher's name: ")
    periods = int(input('Enter the number of periods: ')) 
    rate = int(input('Enter the rate per period: '))
    extra = periods - 100
    extraPeriods = periods - extra
    
    if periods > 100:          
        return f'\nTeacher: {teacher}\nPeriods: {periods}\nGross Salary: {extraPeriods * rate + (extra * 25):,}'  
    else: 
        return f'\nTeacher: {teacher}\nPeriods: {periods}\nGross Salary: {periods * rate:,}'        
    
print(your_salary())
