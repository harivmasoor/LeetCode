from collections import deque, defaultdict
​
def closest_carrot(grid, starting_row, starting_col):
  visited = defaultdict(set)
  return bfs((starting_row, starting_col, 0), grid, visited)
  
def bfs(coords, grid, visited):
  queue = deque([coords])
  dirs = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
  )
  while queue:
    row_i, col_i, depth = queue.popleft()
    for dir in dirs:
      x, y = dir
      new_coord = (row_i + x, col_i + y, depth+1)
      x, y, new_depth = new_coord
      if inbounds(new_coord, grid) and grid[x][y] == 'O' and y not in visited[x]:
        queue.append(new_coord)
        visited[x].add(y)
      elif inbounds(new_coord, grid) and grid[x][y] == 'C':
        return new_depth
  return -1
        
def inbounds(coords, grid):
  row_i, col_i, depth = coords
  if row_i < 0 or row_i > len(grid) - 1:
    return False
  if col_i < 0 or col_i > len(grid[0]) - 1:
    return False
  return True