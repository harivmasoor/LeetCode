from collections import defaultdict, deque
def island_count(grid):
  result = 0
  visited = defaultdict(set)
  for i, r in enumerate(grid):
    for j, root in enumerate(r):
      if root == 'L' and j not in visited[i]:
        bfs((i,j), visited, grid)
        result += 1
  return result
​
def bfs(coords, visited, grid):
  dirs = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
  )
  queue = deque([coords])
  while queue:
    row_i, col_i = queue.popleft()
    visited[row_i].add(col_i)
    for dir in dirs:
      x, y = dir
      new_coord = (row_i + x, col_i + y)
      x, y = new_coord
      if inbounds(new_coord, grid) and grid[x][y] == 'L' and y not in visited[x]:
        queue.append(new_coord)
        
        
def inbounds(coords, grid):
  row_i, col_i = coords
  if row_i < 0 or row_i > len(grid) - 1:
    return False
  if col_i < 0 or col_i > len(grid[0]) - 1:
    return False
  return True