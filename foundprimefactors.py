'''
def factors(value):
    factor = []
    while value >1:
        if value == 1:
            factor.append(1)
            break
        elif value % 2 == 0:
            value = value/2
            factor.append(2)
        elif value%3 == 0:
            value = value/3 
            factor.append(3)
        else:
            factor.append(value)
            break
    return factor
'''
# so this is my first thought it works for small prime numbers but not give expected 
# output as expected for large numbers

            
            # this i write down with some help but it will also not correct for large numebrs 
def factors(value):
    factor = []
    if value == 1:
        factor.append(1)
    for i in range(2,1000):
        while  value % i == 0:
            factor.append(i)
            value  = value//i 
    return factor       
 #  so incrase the range or you can say search space

def factors(value):
    factor = []
    if value == 1:
        factor.append(1)
    for i in range(2,3*int(value**0.5)+1):
        while  value % i == 0:
            factor.append(i)
            value  = value//i 
    return factor
    # so now this coreect form and take upto large values


def factors(value):
    factor = []
    i = 1
    while i < value:
        while value %i ==0:
            factor.append(i)
            value = value//i
            i =i+1
    return factor
            
          