# fractional part of sqrt 2 till 100 decimals
frac_sqrt_2_till_100 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def find_floor_sum(sum_till):
    """
    Recursive function to find the floor sum as defined in the problem.
    """
    if sum_till < 1:
        return 0
    
    elif sum_till == 1:
        return 1
    
    sum_till_complement = frac_sqrt_2_till_100*sum_till//(10**100)
    return (sum_till*sum_till_complement) + (sum_till*(sum_till+1)/2) - (sum_till_complement*(sum_till_complement+1)/2) - find_floor_sum(sum_till_complement)
    
    
def solution(s):
    """
    A detailed mathematical explanation of the used concept can be found at the below link:

    https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
    """
    sum_till = int(s)
    return str(int(find_floor_sum(sum_till)))
