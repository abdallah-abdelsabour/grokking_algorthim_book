

def reverse(arr):
  
     i = 0
     j = len(arr)-1
     while i  < j :
        arr[i],arr[j] = arr[j] ,arr[i]
        i +=1
        j-=1
     return arr


def reverse_recursive(arr,start,end):
     if start <= end :
      arr[start], arr[end ] = arr[end], arr[start]
      reverse_recursive(arr, start+1, end-1)
     return arr

# result = reverse([1,2,3,4,5,6,7,8,9,10])  
lst = [1,2,3,4,5,6,7,8,9,10]
result = reverse_recursive(lst , 0 , len(lst)-1)       
print(result)