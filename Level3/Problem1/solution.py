def solution(l):
    """
    Main driver function for the solution.
    
    :param l: List of numbers
    :type l: List[int]
    :return: Number of lucky triplets
    :rtype: int
    """
    # Store length of the list of numbers since function calls are expensive
    total_nums = len(l)
    # Memoization step: initially store 0 number of divisors for all numbers in the list
    num_divisors = [0 for _ in xrange(total_nums)]
    triplet_count = 0
    
    for indexOuter, eleOuter in enumerate(l):
        # Only uptil indexOuter in inner loop to maintain i<j<k condition
        for indexInner, eleInner in enumerate(l[:indexOuter]):
            if eleOuter % eleInner == 0:
                # increase number of divisor for eleOuter
                num_divisors[indexOuter] += 1
                # Increase triple count by number of divisor of current divisor
                triplet_count += num_divisors[indexInner]
    
    return triplet_count
