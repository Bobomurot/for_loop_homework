def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    l = []
    for name in list1:
        l.append(name[0].upper()+name[1:])
    return l