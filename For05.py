def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    arry = []
    for _ in range(B, A-1, -1):
        arry.append(_)
    return arry