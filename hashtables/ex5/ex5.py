# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    table = build_lookup_table(files)
    result = []
    for q in queries:
        if table.get(q) is not None:
            result += table.get(q)
    return result


def build_lookup_table(files):
    table = {}
    for item in files:
        split = item.split("/")
        if table.get(split[-1]) is None:
            table.update({split[-1]:[item]})
        else:
            table.update({split[-1]:table.get(split[-1])+[item]})
    return table


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
