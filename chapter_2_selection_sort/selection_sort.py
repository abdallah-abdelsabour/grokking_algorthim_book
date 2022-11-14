# big O =>> O(n^2)   for selction sort 

# sort array in way 



def find_smallest(arre):
  smallest = arre[0]
  smallest_indx=0
  for indx in range(len(arre)):
    if arre[indx]< smallest :
      smallest = arre[indx]
      smallest_indx = indx
  return smallest_indx
      


# selction sort function 
def selection_sort(arr):
  new_arry = []
  smallest = arr[0]
  for indx in range(len(arr)):
    smallest = find_smallest(arr)
    new_arry.append(arr.pop(smallest))
  return new_arry
if __name__ == "__main__":
    arr = [100,200,200,400,40]
    result =  selection_sort(arr)
    print(result)