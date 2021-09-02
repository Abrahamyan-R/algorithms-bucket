from collections import deque

maze = [
  [1, 0, 0, 1, 1, 1],
  [1, 1, 1, 0, 0, 1],
  [0, 1, 0, 1, 1, 0],
  [0, 1, 1, 1, 1, 0],
  [1, 0, 0, 0, 1, 0],
  [0, 0, 1, 1, 1, 1],
]

ROWS_COUNT = len(maze)
COLS_COUNT = len(maze[0])

neighbours_couples = [
  (0, -1),
  (0, 1),
  (-1, 0),
  (1, 0),
]

visited = []

for i in range(ROWS_COUNT):
  visited.append([])
  for j in range(COLS_COUNT):
    visited[i].append(False)

class Point:
  def __init__(self, x, y):
      self.x = x
      self.y = y

class GraphElement:
  def __init__(self, point: Point, distance: int):
      self.point = point
      self.distance = distance

def is_correct_point(x: int, y: int) -> bool:
  if x < 0 or x >= ROWS_COUNT or y < 0 or y >= COLS_COUNT:
    return False

  return True


def find_path(maze, startPoint: Point, endPoint: Point):
  if maze[startPoint.x][startPoint.y] == 0 or maze[endpoint.x][endpoint.y] == 0:
    return -1

  neighbours = deque()

  root = GraphElement(startPoint, 0)
  neighbours.append(root)
  visited[startPoint.x][startPoint.y] = True
  
  while(neighbours):
    curr_point: GraphElement = neighbours.popleft()
    point: Point = curr_point.point
    
    if point.x == endpoint.x and point.y == endpoint.y:
      return curr_point.distance
    
    for neighbour in neighbours_couples:
      new_point_x = point.x + neighbour[0]
      new_point_y = point.y + neighbour[1]

      if is_correct_point(new_point_x, new_point_y) and not visited[new_point_x][new_point_y]:
        new_point = Point(new_point_x, new_point_y)
        new_graph_element = GraphElement(new_point, curr_point.distance + 1)

        neighbours.append(new_graph_element)
        visited[new_point_x][new_point_y] = True

  return -1


startPoint = Point(0, 0)
endpoint = Point(5, 5)

distance = find_path(maze, startPoint, endpoint)
print("distance -> ", distance)