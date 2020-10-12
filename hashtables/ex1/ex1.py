def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hash_table = build_lookup_table(weights, length)
    for weight in hash_table.keys():
        difference = limit - weight
        if difference < 0:
            continue
        first_index = hash_table.get(weight)
        if type(first_index) is list:
            first_index = first_index[0]
        second_index = hash_table.get(difference)
        if type(second_index) is list:
            second_index = second_index[1]
        if second_index is not None:
            return (first_index,second_index) if first_index>second_index else (second_index,first_index)
    return None


def build_lookup_table(weights, length):
    hash_table = {}
    for i in range(length):
        if hash_table.get(weights[i]) is None:
            hash_table.update({weights[i]:i})
        else:
            l = [hash_table.get(weights[i])]
            hash_table.update({weights[i]:l+[i]})
    return hash_table
