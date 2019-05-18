# given a list of tuples, merge the overlapping ranges as shown:
# [(1,6), (0,5), (7,10)] -> [(0,6), (7,10)]

def merge(mylist):

    mylist.sort(key = lambda x: x[0])
    results = []

    for e in mylist:

        if not results:
            results.append(e)

        else:
            last = results[-1]

            if e[0]<=last[1]:

                lower = last[0]
                higher = max(e[1], last[1])
                results[-1]=(lower, higher)
            else:
                results. append(e)
                
    return results

# driver code
mylist = [(1,2), (0,5), (2,4), (5,6), (5,6)]
print(merge(mylist))