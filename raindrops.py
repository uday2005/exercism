def convert(number):
    why =  []
    if number %3 ==  0 :
        why.append("Pling")
    if number % 5 == 0:
        why.append("Plang")
    if number % 7 == 0:
        why.append("Plong")
    why1 = "".join(why)
    return why1 if why1 else str(number)

    if why:
        return "".join(why)
    else:
        return str(number)


# but the problem here is happening when the number is divisble by both 3 and 5 
# it should brong plingplang but it is not happening  

# so to do that we can use if caondtion all the way as elif only gets activated if the if statement is false

# the next problem will be when we will use else right before it check onlt the case in which number %7 ==0

# we use the .join function for dictionary

