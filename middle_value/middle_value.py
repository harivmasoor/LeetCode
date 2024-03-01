# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def middle_value(head):
  fast = head
  slow = head
  while fast.next is not None:
    if fast.next.next is not None:
      fast = fast.next.next
      slow = slow.next
      print("fast", fast.val)
      print("slow", slow.val)
    else:
      return slow.next.val
  return slow.val
​