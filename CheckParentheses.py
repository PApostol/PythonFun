def check_parentheses(expression): 
      
    mymap = {'(':')', '{':'}','[':']'}
    mylist = []

    for letter in expression:
        if letter in mymap:
            mylist.append(mymap[letter])

        elif letter in mymap.values():
            if not mylist or letter != mylist.pop():
                return False

    # True only if mylist is empty
    return not mylist