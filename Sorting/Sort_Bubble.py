# O(n^2)
def bubble_sort(mylist):
  n = len(mylist)

  for i in range(n):
    for j in range(i, n):
        
      if mylist[i]>mylist[j]:
        mylist[i], mylist[j] = mylist[j],mylist[i]

  return mylist