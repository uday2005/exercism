def convert(number):
    why = []
    if number %3 ==  0 :
        why.append("Pling")
    elif number % 5 == 0:
        why.append("Plang")
    elif number % 7 == 0:
        why.append("Plong")
    else:
        return str(number)
    return why[0]