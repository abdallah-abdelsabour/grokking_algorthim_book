
def binary_search(lst , target):
  low  = 0
  high = len(lst)- 1 
  while high >= low:
    mid = (low + high )// 2
    if lst[mid] == target:
      return mid
    elif lst[mid] > target :
      high = mid -1
    else :
      low = mid +1
  return None


result = binary_search([1,2,3,4,5,6,10,15,48], 15)

print( result)     



