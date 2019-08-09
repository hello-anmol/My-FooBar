from collections import deque

class Coordinates:
    """Object to store the coordinates in catesian."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        """Define "+" arithematic operation for Coordinates."""
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Coordinates(new_x, new_y)
    
    def __eq__(self, other):
        """Define equality operation for Coordinates."""
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __hash__(self):
        """Defined hashed value for coordinates for use as dictionary key."""
        return (self.x ^ self.y) + (self.x + self.y)

class Node:
    """Object to store each cell and it's corresponding details."""
    def __init__(self, coordinates, depth):
        self.coordinates = coordinates
        self.depth = depth
    
    def __eq__(self, other):
        """Define equality operation for Nodes."""
        if self.coordinates == other.coordinates:
            return True
        return False
        
class Grid:
    """Class to manage grid operations such as finding neighbours etc."""
    def __init__(self, map):
        self.map = map
        self.width = len(map)
        self.height = len(map[0])
        self.allowed_dirs = [Coordinates(0, 1), Coordinates(0, -1), Coordinates(1, 0), Coordinates(-1, 0)]
        # Store visited walls in dictionary to avoid O(n) lookup complexity
        self.visited = {}
        self.walls = []
        
    def isWall(self, coordinates):
        """Helper method to tell if the given coordinates represents a wall in the grid."""
        if self.map[coordinates.x][coordinates.y] == 1:
            return True
        return False
    
    def getNeighbours(self, node):
        """Get valid neighbours of the passed node."""
        neighbours = []
        for dir_coord in self.allowed_dirs:
            new_coord = node.coordinates + dir_coord
            # Ignore if the generated coordinate is not inside the grid
            if self.isValidCoord(new_coord):
                if self.visited.get(new_coord, 0) == 0:
                    self.visited[new_coord] = 1
                    neighbours.append(Node(new_coord, node.depth + 1))
        return neighbours
    
    def isValidCoord(self, coordinates):
        """Helper method to check if the coordinates lie inside the grid."""
        if (0 <= coordinates.x < self.width) and (0 <= coordinates.y < self.height):
            return True
        return False

def solverToWall(grid, node):
    """
    Breadth First Search to all the walls from given node. No walls are crossed.
    
    :param grid: Grid to be solved for
    :type grid: Grid
    :param node: Node to start BFS with
    :type node: Node
    """
    import time
    # Store distances to each wall encountered
    distances = {}
    queue = deque([])
    queue.append(node)
    while queue:
        cur_node = queue.popleft()
        # If wall encountered, note depth and the coordinates
        if grid.isWall(cur_node.coordinates):
            grid.walls.append(cur_node.coordinates)
            distances[cur_node.coordinates] = cur_node.depth - 1
        else:
            # Append neighbours to the queue
            queue.extend(grid.getNeighbours(cur_node))
    return distances

def solution(map):
    """
    Main driver function for the solution.
    
    :param map: 2-D list of Integers denoting walls and passes
    :type map: List[List[Int]]
    :return: Minimum number of steps to reach end from start
    :rtype: int
    """
    grid = Grid(map)
    start_node = Node(Coordinates(0, 0), 1)
    end_node = Node(Coordinates(grid.width - 1, grid.height - 1), 1)
    # Distance to each first wall from start node
    wall_distances_from_start = solverToWall(grid, start_node)
    # Coordinates of each first wall from start node
    walls_from_start = set(grid.walls)
    grid.walls = []
    grid.visited = {}
    # Distance to each first wall from end node
    wall_distances_from_end = solverToWall(grid, end_node)
    # Walls first to both start node and end node
    common_walls = walls_from_start & set(grid.walls)
    min_distance = 1e9
    for wall in common_walls:
        min_distance = min(min_distance, wall_distances_from_end[wall] + wall_distances_from_start[wall] + 1)
    return min_distance
