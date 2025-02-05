def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    arry = []
    for i in range(n+1):
        arry.append(i)
        i += 1
    return arry
