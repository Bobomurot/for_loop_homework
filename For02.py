def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    arry = []
    for i in range(n+1):
        arry.append(str(i))
        i += 1
        x = " ".join(map(str, arry))
    return x