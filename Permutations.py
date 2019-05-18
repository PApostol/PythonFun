# given a list, print all possible permutations of its elements

def permutation(mylist):

  if len(mylist) == 0: 
      return [] 

  elif len(mylist) == 1: 
      return [mylist] 

  ans = [] # empty list that will store current permutation 

  for i in range(len(mylist)): 
      element = mylist[i]

      # Extract mylist[i] or element from the list
      rem_list = mylist[:i] + mylist[i+1:]
      print(mylist[:i])
      print(mylist[i+1:])

      # Generating all permutations where element is first 
      for perm in permutation(rem_list):
        if [element]+perm not in ans: # for unique permutations
          ans.append([element] + perm)

  return ans


# driver code
inp = '123'
res = permutation(list(inp))

for e in res:
  print(''.join(e))