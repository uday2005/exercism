def count_words(sentence):
    dict = {}
    why = sentence.split()
    for item in why:
        item = item.strip(",!.'$&:%^")
        item = item.lower()
        if item not in dict:
           dict[item]  = 1
        else:
           dict[item] +=1
    return dict


#this is like the first first approch with help of ai

# so we learned here one thing that we can strip multiple thing from string 
# item = item.strip("wh@")

#BUT STRIP ONLY REMOVE THE ELEMENT FROM FRONT AND BACK SIDE LIKE NOT IN MIDDLE CHARACTERS

# SO THE PROBELM IS WE ARE UNABLE TO USE WE CAN USE MULTIPLE SPLIT LIKE IN UNDERSCORE AND COMMA WHICH IS NOTFEASIBLE 

#SO WHAT IS DONE HERE IS REPLACE THAT CHARACTER WITH SPACE  AND THEN SPLIT WITH SPACE


def count_words(sentence):
    dict = {}
    why = sentence.replace("_"," ")   # replace underscore with space
    why = why.replace("\n"," ")       # replace \n with space
    why = why.replace(","," ")        # replace , with space
    why = why.split()                 #split at space
    for item in why:                  # for accesing the list and iterating over the list
        item = item.strip(",!.'$&:%^@")   # remove the unwanted chracter
        item = item.lower()               #lower all word so that it will be case insensitive
        if item not in dict:           # if item not in dict then add that value in dict 
           dict[item]  = 1
        else:
           dict[item] +=1   # if already item in dict then increase the count of value of dict
    return dict