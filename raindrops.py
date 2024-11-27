def convert(number):
    why = []
    if number %3 ==  0 :
        why.append("Pling")
        print(why)
    elif number % 5 == 0:
        why.append("Plang")
        print(why)
    elif number % 7 == 0:
        why.append("Plong")
        print(why)
    else:
        return str(number)
    return why[:-1]

# but the problem here is happening when the number is divisble by both 3 and 5 
# it should brong plingplang but it is not happening  
convert(3)
convert(5)
convert(7)
convert(43)
convert(105)