# O(nlogn)
def merge_sort(mylist):
    if len(mylist) < 2:
      return mylist

    less = []
    equal = []
    greater = []
    
    n = int(len(mylist)/2)
    pivot = mylist[n]

    for x in mylist:
      if x < pivot:
          less.append(x)
      elif x == pivot:
          equal.append(x)
      elif x > pivot:
          greater.append(x)

    return merge_sort(less) + equal + merge_sort(greater)