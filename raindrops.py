# def convert(number):
#     why =  []
#     if number %3 ==  0 :
#         why.append("Pling")
#     if number % 5 == 0:
#         why.append("Plang")
#     if number % 7 == 0:
#         why.append("Plong")
#     why1 = "".join(why)
#     return why1 if why1 else str(number)

     # that return statement expanded version
    #if why:
        #return "".join(why)
    #else:
        #return str(number)


# but the problem here is happening when the number is divisble by both 3 and 5 
# it should brong plingplang but it is not happening  

# so to do that we can use if caondtion all the way as elif only gets activated if the if statement is false

# the next problem will be when we will use else right before it check onlt the case in which number %7 ==0

# we use the .join function for dictionary
```python
def convert(number):
    why = ""

    if number %3 ==  0 :
        why += "Pling"
    if number % 5 == 0:
        why += "Plang"
    if number % 7 == 0:   
        why += "Plong"

    if why:
        return why
    else:
        return str(number)
```

def convert(number):
    result = []
    rules = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
        # Add more rules as needed
    }
    for divisor,sound in rules.items():
        if number % divisor == 0:
            result.append(sound)
    if result:
        return "".join(result)
    else:
        return str(number)

# so here the problem with above two code is it is good for th esmaller problem bu tnot fo r
# not for large problems like we have to write 100 iff statemnets like mathces 100 factor 3 57 12 14 so 
# # this dict method is usefuk there
# taken help by chat-gpt in writing last code  