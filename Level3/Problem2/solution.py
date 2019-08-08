def solution(n):
    """
    Main driver function for the solution.
    
    :param n: Long Integer
    :type n: str
    :return: Minimum number of steps
    :rtype: int
    """
    # retrieve long int from string
    n = long(n)
    steps = 0
    # use binary arithematic for optimized operations
    while (n != 1):
        if not n & 1:
            n = n >> 1
        # If right trailing zeroes are less in n+1 than n-1, use n-1 since more division operations possible in next step
        # 3 is an exception
        elif (trailing_zeros(bin(n+1)) < trailing_zeros(bin(n-1))) or (n == 3):
            n -= 1
        else:
            n += 1
        steps += 1
    
    return steps
    
def trailing_zeros(bin_num):
    """
    Return the number of trailing zeros of a binary number.
    
    :param bin_num: Binary number
    :type bin_num: str
    """
    num_trailing_zeros = 0
    for ele in bin_num[::-1]:
        if ele != '0':
            break
        num_trailing_zeros += 1
    return num_trailing_zeros
