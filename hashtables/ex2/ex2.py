#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                        )


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    start = None
    for ticket in tickets:
        if ticket.source == 'NONE':
            start = ticket.destination
        hash_table_insert(ht, ticket.source, ticket.destination)
    route[0] = start
    for i in range(length - 1):
        print(route[i])
        route[i + 1] = hash_table_retrieve(ht, route[i])

    return route
