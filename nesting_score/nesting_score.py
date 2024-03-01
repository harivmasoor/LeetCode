def nesting_score(string):
  stack = [0]
  for char in string:
    if char == '[':
      stack.append(0)
    else:
      if stack:
        last_var = stack.pop()
        if last_var > 0:
          stack[-1]+=2*last_var
        else:
          stack[-1]+=1
  return stack[0]
​