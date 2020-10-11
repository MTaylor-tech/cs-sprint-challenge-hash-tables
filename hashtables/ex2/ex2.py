#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_table = {}
    for t in tickets:
        ticket_table.update({t.source:t.destination})
    d = ticket_table.get("NONE")
    route = [d]
    while d != "NONE":
        d = ticket_table.get(d)
        route.append(d)
    return route
