def is_prime(n):
  array=[]
  if n ==1:
    return False
  for num in range(2,n):
    array.append(num)
  for num2 in array:
    if n % num2 == 0:
      return False
  return True
  
    