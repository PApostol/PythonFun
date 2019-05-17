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