from itertools import permutations, combinations


def optimize_with_floyd(graph_mat):
    """
    Use Floyd-Warshall's algorithm to find the shortest path between every two node of the graph.
    
    :param graph_mat: Graph in matrix format
    :type graph_mat: List[List[Int]]
    :return: Optimized graph matrix with shorted paths
    :rtype: List[List[Int]]
    """
    num_nodes = len(graph_mat)
    for src in graph_mat:
        for dest_ind, _ in enumerate(src):
            for intmed_ind, intmed in enumerate(graph_mat):
                # If path using intermediate node is shorter, update distance
                if src[intmed_ind] + intmed[dest_ind] < src[dest_ind]:
                    src[dest_ind] = src[intmed_ind] + intmed[dest_ind]
        
                    
def has_negative_cycle(graph_mat):
    """
    Check if the graph has a negative cycle.
    
    Uses the property that weight of reaching i from i becomes negative in Floyd-Warshal
    if graph has a negative cycle.
    
    :param graph_mat: Graph in matrix format
    :type graph_mat: List[List[Int]]
    :return: True if has negative cycle, False otherwise
    :rtype: Bool
    """
    for index in xrange(len(graph_mat)):
        if graph_mat[index][index] < 0:
            return True
    return False

def get_super_set(set):
    """
    Get super set of the provided set.
    
    :param set: The original set
    :type set: List
    :return: The power set of the given set excluding null set
    :rtype: List[List]
    """
    power_set = []
    for num in xrange(1, len(set)+1):
        power_set.extend([list(comb) for comb in combinations(set, num)])
    return power_set
    
def find_max_bunnies(graph_mat, num_bunnies, time_limit):
    """
    Find the maximum number of bunnies that can be rescued.
    
    :param graph_mat: Graph in matrix format
    :type graph_mat: List[List[Int]]
    :param num_bunnies: Total number of bunnies
    :type num_bunnies: Int
    :param time_limit: Remaining time before door shuts
    :type time_limit: Int
    :return: List of maximum bunnies that can be rescued
    :rtype: List[Int]
    """
    optimal = []
    # Get all possible set of bunnies that can be picked
    all_combinations = get_super_set([num for num in xrange(num_bunnies)])
    # Sort in order to go from higher to smaller in order to optimize
    all_combinations.sort(key=lambda x: len(x),reverse=True)
    for combination in all_combinations:
        for perm in permutations(combination):
            source = 0
            time_taken = 0
            for bunny in perm:
                dest = bunny + 1
                time_taken += graph_mat[source][dest]
                source = dest
            # Going with all bunnies to bulkhead
            time_taken += graph_mat[source][num_bunnies+1]
            if time_taken <= time_limit and len(perm) > len(optimal):
                optimal = perm
                break

    return sorted(list(optimal))
    
def solution(times, time_limit):
    """
    Main driver function for the solution.
    
    :param times: Graph for the problem in matrix form
    :type times: List[List[Int]]
    :param time_limit: Time before bulkhead closes 
    :type map: Int
    :return: List of maximum bunnies that can be rescued
    :rtype: List[Int]
    """
    # find optimal time between two nodes using Floyd-Warshall algorithm
    optimize_with_floyd(times)
    num_bunnies = len(times) - 2
    # If graph has negative cycles, all bunnies can be picked up
    if has_negative_cycle(times):
        return [num for num in xrange(num_bunnies)]
    else:
        return find_max_bunnies(times, num_bunnies, time_limit)
