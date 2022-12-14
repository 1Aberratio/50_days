# Day 22 : Add Under_Score

def add_hash(h_str):
    return '#'.join(h_str)
    
def add_underscore(u_str):
    return u_str.replace('#','_')
    
def remove_underscore(r_u_str):
    return r_u_str.replace('_','')

w_str = "Python"
print(add_hash(w_str))
print(add_underscore(add_hash(w_str)))
print(remove_underscore(add_underscore(add_hash(w_str))))
