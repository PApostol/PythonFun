import time, copy
from random import randint

# O(kn)
def radix_sort(mylist):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range(RADIX)]
 
    # split aList between lists
    for i in mylist:
      tmp = i // placement
     
      buckets[tmp % RADIX].append(i)
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range(RADIX):
      buck = buckets[b]
      for i in buck:
        mylist[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX


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


# O(n^2)
def bubble_sort(mylist):
  n = len(mylist)

  for i in range(n):
    for j in range(i, n):
      if mylist[i]>mylist[j]:
        mylist[i], mylist[j] = mylist[j],mylist[i]

  return mylist


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



n = 20000
mylist1 = [randint(0, n) for i in range(n)]
mylist2 = copy.deepcopy(mylist1)
mylist3 = copy.deepcopy(mylist1)
mylist4 = copy.deepcopy(mylist1)
mylist5 = copy.deepcopy(mylist1)

start = time.time()
bubble_sort(mylist1)
stop = time.time()
print('Bubble sort: {:0.6f} s\n'.format(stop - start))


start = time.time()
selection_sort(mylist2)
stop = time.time()
print('Selection sort: {:0.6f} s\n'.format(stop - start))


start = time.time()
merge_sort(mylist3)
stop = time.time()
print('Merge sort: {:0.6f} s\n'.format(stop - start))
  
start = time.time()
insertion_sort(mylist4)
stop = time.time()
print('Insertion sort: {:0.6f} s\n'.format(stop - start))

start = time.time()
radix_sort(mylist5)
stop = time.time()
print('Radix sort: {:0.6f} s\n'.format(stop - start))