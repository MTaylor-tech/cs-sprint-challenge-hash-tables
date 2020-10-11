def intersection(arrays):
    """
    YOUR CODE HERE
    """
    l = len(arrays)
    r = []
    table = build_lookup_table(arrays,l)
    for k in table.keys():
        if table.get(k) == l:
            r.append(k)
    return r


def build_lookup_table(arrays,length):
    table = {}
    counter = 1
    for arr in arrays:
        for item in arr:
            if counter==1:
                table.update({item:1})
            elif table.get(item)==counter-1:
                table.update({item:table.get(item)+1})
        counter += 1
    # print(f"{table[1],table[2],table[3]}")
    return table


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
