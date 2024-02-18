from collections import defaultdict
​
def semesters_required(num_courses, prereqs):
  if not prereqs:
    return 1
  graph = build_graph(prereqs)
  return longest_path(graph)
​
def build_graph(prereqs):
  graph = defaultdict(list)
  for edge in prereqs:
    f, t = edge
    graph[t].append(f)
  print(graph)
  return graph
​
def longest_path(graph):
  memo = {}
  res = 0
  def dfs(node, visited, depth):
    if node in memo:
      return memo[node]
    else:
      if node in visited:
        return memo[node]
      elif node in set(graph.keys()):
        visited.add(node)
        max_depth = 0
        for neighbor in graph[node]:
          max_depth = max(max_depth, dfs(neighbor, visited, depth))
        memo[node] = max_depth + 1
        return memo[node]
      else:
        visited.add(node)
        memo[node] = depth
        return depth
  for root in graph.keys():
    print(graph)
    res = max(res, dfs(root, set(), 1))
    print(graph)
  return res