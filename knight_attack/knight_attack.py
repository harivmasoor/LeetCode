from collections import deque, defaultdict
def knight_attack(n, kr, kc, pr, pc):
  return bfs(n, kr, kc, pr, pc)
def bfs(n, kr, kc, pr, pc):
  visited = defaultdict(set)
  dirs = [
    (1,2),
    (2,1),
    (-1,2),
    (2,-1),
    (1,-2),
    (-2,1),
    (-1,-2),
    (-2,-1),
  ]
  queue = deque([(kr, kc, 1)])
  while queue:
    row_i, col_i, depth = queue.popleft()
    for dir in dirs:
      new_row = row_i + dir[0]
      new_col = col_i + dir[1]
      if inbounds(new_row, new_col, n):
        if new_row == pr and new_col == pc:
          return depth
        elif not new_col in visited[new_row]:
          visited[new_row].add(new_col)
          queue.append((new_row, new_col, depth+1))
  return None
      
def inbounds(row_i, col_i,n):
  if 0<=row_i<n and 0<=col_i<n:
    return True
  return False
    
    visited[row_i].add(col_i)