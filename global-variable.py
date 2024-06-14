l= float(input('enter a lenght:'))
w= float(input('enter a width:'))

def area ():
    # h = float(input('enter a height:'))
    global area_of_object
    area_of_object= l*w
    
    return area_of_object

def volume():
    h= float(input('enter a height:'))
    v= area_of_object* h
    return v 

result_r  = area()
result = volume()
print(result_r)
print(result)



