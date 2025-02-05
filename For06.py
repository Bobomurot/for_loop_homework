def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    arry = []
    for i in range(A, B):
        arry.append(i)
    return sum(arry)