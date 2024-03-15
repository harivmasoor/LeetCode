def subsets(elements):
  if not elements:
    return [[]]
  subs_without_first = subsets(elements[1:])
  subs_with_first=[]
  for sub in subs_without_first:
    subs_with_first.append([elements[0],*sub])
  return subs_with_first + subs_without_first