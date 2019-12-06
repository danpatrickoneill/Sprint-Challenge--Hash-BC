#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)

    for i, weight in enumerate(weights):
        solution_index = hash_table_retrieve(ht, limit - weight)
        if solution_index:
            if i >= solution_index:
                return (i, solution_index)
            else:
                return (solution_index, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
