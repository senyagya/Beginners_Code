
def myfunc(string):
    new_string =""
    index =0
    for c in string:
        if(index%2 ==0):
            new_string += c.upper()
            index += 1
        else:
            new_string += c.lower()
            index += 1
    return new_string