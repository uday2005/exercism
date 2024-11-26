def square(number):
    try:
        if number not in range(1,65):
            raise ValueError("square must be between 1 and 64")
        
        #if number is not in between 1 and 64 then return rasie Valuerror
        if number == 1:
            return 1
        # I AM USING RECURSSION CONCEPT AND UP IS DEFIEND AS BASE CASE
        else:
            return square(number-1) *2
        # THE NOW THE UP ONE IS RECURSSIVE STEPS
    except:
        raise ValueError("square must be between 1 and 64")


def total():
    sum =0
    for i in range (1,65):
        why = square(i)
        sum  += why
    return sum
        

# ONE THING THAT I  AM NOT STILL CLEAR IS THAT TRY AND EXCEPT AS 
# I AM UNABLE   TO UNDERSTAND ITS SO I MUST READ ABOUT IT


    
    
