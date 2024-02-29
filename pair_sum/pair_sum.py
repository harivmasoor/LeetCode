def pair_sum(numbers, target_sum):
  hashmap = {}
  for i, num in enumerate(numbers):
    compliment = target_sum - num
    if compliment in hashmap:
      return (hashmap[compliment],i)
    else:
      hashmap[num] = i
​
    
    