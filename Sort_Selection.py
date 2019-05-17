# O(n^2)
def selection_sort(mylist):
  maxi = max(mylist)
  n = 0

  while n<len(mylist):
    mini = maxi
    index = n
    swap = None

    for i in range(n, len(mylist)):
      if mylist[i] <= mini:
        mini = mylist[i]
        swap = index

      index+=1
    
    mylist[n], mylist[swap] = mylist[swap], mylist[n]
    n+=1

  return mylist