def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    arry = []
    for i in range(N+1):
        if i % 2 != 0:
            arry.append(i)
            i += 1
        
    return sum(arry)