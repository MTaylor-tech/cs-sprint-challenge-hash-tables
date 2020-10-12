def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = build_lookup_table(a)
    result = []
    for k,v in table.items():
        if v:
            result.append(k)
    return result


def build_lookup_table(data):
    table = {}
    for item in data:
        if item < 0:
            item = abs(item)
        if table.get(item) is None:
            table.update({item:False})
        elif table.get(item)==False:
            table.update({item:True})
    return table


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
