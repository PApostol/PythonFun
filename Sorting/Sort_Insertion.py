# O(n^2)
def insertion_sort(mylist):
  
  for i in range(1,len(mylist)):

    j=i-1
    k = i

    while mylist[k]<mylist[j] and j>=0:
      mylist[k], mylist[j] = mylist[j], mylist[k]
      k= j
      j-=1

  return mylist