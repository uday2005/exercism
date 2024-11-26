def is_armstrong_number(number):
    count = 0
    for why in str(number):
        count +=1
    
    sum = 0
    for int1 in str(number):   # converting the int to string and iterating ove rthat string an dget thta string
        int2 = int(int1)       # no wwe get that string but we have to change it to int to use ** thus as it is not done on string
        sum += int2**count

    if sum == number:
        return True
    else:
        return False
        
  # here i want to keep count of how many digits are there in the integer  as we need that power up to each integer
  # as we proceed further what we are know that int is non iteratable.
  # so we are first converting int to string and then iterating over string and keep count of that


