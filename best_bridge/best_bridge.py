
      if grid[row_i][col_i]=="L":
        return find_island_bfs((row_i,col_i), grid)
    
def find_island_bfs(incoming_coords, grid):
  visited = set()
  island_coords = []
  queue = deque([incoming_coords])
  while queue:
    coords = queue.popleft()
    visited.add(coords)
    island_coords.append(coords)
    row, col = coords
    for dir in DIRS:
      new_row = row + dir[0]
      new_col = col + dir[1]
      new_coords = (new_row, new_col)
      if inbounds(new_coords, grid) and grid[new_row][new_col]=="L" and not new_coords in visited:
        queue.append(new_coords)
  return island_coords
​
def build_bridge_bfs(incoming_coords, grid, island_coords):
  visited = set()
  queue = deque([(incoming_coords[0], incoming_coords[1], -1)])
  while queue:
    coords = queue.popleft()
    row, col, depth = coords
    visited.add((row, col))
    depth += 1
    for dir in DIRS:
      new_row = row + dir[0]
      new_col = col + dir[1]
      new_coords = (new_row, new_col)
      if inbounds(new_coords, grid) and grid[new_row][new_col]=="L" and not new_coords in island_coords:
        return depth
      elif inbounds(new_coords, grid) and grid[new_row][new_col]=="W" and not new_coords in visited:
        queue.append((new_row, new_col, depth))
        
def inbounds(coords, grid):
  row,col = coords
  if  0 <= row < len(grid) and 0 <= col < len(grid[0]):
    return True
  return False
    
    