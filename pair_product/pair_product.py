def pair_product(numbers, target_product):
  hashmap={}
  for i, num in enumerate(numbers):
    compliment = (target_product/num)
    if compliment in hashmap:
      return (hashmap[compliment], i)
    else:
      hashmap[num] = i