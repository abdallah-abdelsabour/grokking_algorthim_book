
def fact(x):
  if x == 1:
    return 1
  else:
   return x * fact(x-1)
  


result = fact(100)
print(result)