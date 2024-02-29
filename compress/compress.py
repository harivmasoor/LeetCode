def compress(s):
  string = s + "!"
  count = 1
  result = []
  i = 0
  j = 0
  result = []
  while j < len(string)-1:
    if string[j] == string[j+1]:
      count +=1
      j+=1
    else:
      if count == 1:
        result.append(str(string[i]))
        j+=1
        i=j
      else:
        result.append(str(count) + str(string[i]))
        j+=1
        i = j
        count = 1
  return "".join(result)
      
      