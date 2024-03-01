def decompress_braces(string):
  stack = []
  numbers = "123456789"
  result = ''
  for char in string:
    if char in numbers:
      stack.append(int(char))
    elif char == '}':
      segment = ''
      while not isinstance(stack[-1],int):
        popped = stack.pop()
        segment = popped + segment
      number_pop = stack.pop()
      stack.append(number_pop*segment)
    elif not char =='{':
      stack.append(char)
  return "".join(stack)
    
  
​