def solution(n, b):
    """
    Main driver function for the solution
    
    :param n: The first ID in base b
    :type n: str
    :param b: Base for the ID
    :type b: int
    :return: Length of the repeating block
    :rtype: int
    """
    # Using Dict since finding is O(n) as keys are hashed and also order is maintained via num_IDs
    already_assigned_IDs = dict()
    # Maintain number of IDs already added
    num_IDs = 0
    # Find new IDs until we encounter an existing one
    while not already_assigned_IDs.get(n, 0):
        # Add key "n" to OrderedDict with value 1
        num_IDs += 1
        already_assigned_IDs[n] = num_IDs
        # Create an integer list since arithematic operations are easier
        digits_n = [int(ele) for ele in n]
        # Use python's inbuilt sorting which uses Tim Sort
        x = sorted(digits_n, reverse=True)
        y = sorted(digits_n)
        # Call function to subtract y from x in base b
        z = sub_with_base(x, y, b)
        # Assign z to n for next interation
        n = "".join([str(ele) for ele in z])
    # Length of repeating block is (total length) - (number of IDs inserted before repeated ID)
    concerned_length = len(already_assigned_IDs) - (already_assigned_IDs[n] - 1)
    return concerned_length

def sub_with_base(x, y, b):
    """
    Do subtraction in base b.
    
    :param x: The larger (or equivalent) of the two integers.
    :type x: List of integers
    :param y: The smaller (or equivalent) of the two integers.
    :type y: List of integers
    :param b: Base of the integers
    :type b: int    
    :return: Integer after subtracting y from x
    :rtype: List of integers
    """
    # Find length for iteration purposes, calling len() repeatedly is expensive
    k = len(x)
    # Maintain borrowing in subtration
    borrow_list = [0 for _ in xrange(k)]
    result = [0 for _ in xrange(k)]
    # Iterate from right to left of x and y
    for index in xrange(k-1, -1, -1):
        val = x[index] - y[index] - borrow_list[index]
        # If positive value, no updates in borrow list
        if val >= 0:
            result[index] = val
        # If negative value, update borrow list if not the extreme left integer
        else:
            # Result at this index would be val added with Base
            result[index] = val + b
            if index != 0:
                borrow_list[index-1] = 1
                
    return result
