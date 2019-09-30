from fractions import Fraction

def solution(pegs):
    """
    Main driver function for the solution.
    
    :param n: List of peg positions
    :type n: List[int]
    :return: Radius of first gear if exists, [-1, -1] otherwise
    :rtype: List[int, int]
    """
    val = 0
    multiplier = -1
    total_pegs = len(pegs)
    for index, ele in enumerate(pegs):
        val += (multiplier * ele)
        multiplier = multiplier * -1
        # multiplier is -1 for the first element
        if index == 0:
            multiplier = multiplier * 2
        # multiplier will be either -1 or 1 for the last element
        if index == total_pegs - 2:
            multiplier = multiplier / 2
    # if negative value obtained, no solution exists
    if val <= 0:
        return [-1, -1]
    # radius of the first peg, storing as Fraction for easier arithematic operations
    # value of 2 and 2/3 obtained using mathematical equation for odd and even number of pegs respectively
    f_gear_radius = Fraction(2 * (float(val) / 3 if (total_pegs % 2 == 0) else val)).limit_denominator(3)
    
    cur_peg_radius = f_gear_radius
    # Iterate through all pegs and see if any gear radius is becoming less than 1 since that would be invalid
    for index in xrange(total_pegs-2):
        cur_peg_distance = pegs[index + 1] - pegs[index]
        cur_peg_radius = cur_peg_distance - cur_peg_radius
        if cur_peg_radius < 1:
            return [-1, -1]
    
    return [f_gear_radius.numerator, f_gear_radius.denominator]