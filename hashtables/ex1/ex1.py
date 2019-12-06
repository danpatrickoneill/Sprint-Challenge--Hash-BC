#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i, weight in enumerate(weights):
        print(weight, i)
        hash_table_insert(ht, weight, i)
    # for weight in weights:
    #     if hash_table_retrieve(ht, limit - weight):
    #         weight_one = hash_table_retrieve(ht, weight)
    #         weight_two = hash_table_retrieve(ht, limit - weight)
    #         for item in ht.storage:
    #             if item:
    #                 print(item.key, ': ', item.value)
    #         print((weight_one, weight_two))
    #         if weight_one >= weight_two:
    #             return (weight_one, weight_two)
    #         else:
    #             return (weight_two, weight_one)
    for i, weight in enumerate(weights):
        solution_index = hash_table_retrieve(ht, limit - weight)
        if solution_index:
            weight_one = i
            weight_two = solution_index
            if weight_one >= weight_two:
                return (weight_one, weight_two)
            else:
                return (weight_two, weight_one)

    return None

    # for i, weight in enumerate(weights):
    #     print(weight, i)
    #     hash_table_insert(ht, weight, i)
    # for weight in weights:
    #     if hash_table_retrieve(ht, limit - weight):
    #         weight_one = hash_table_retrieve(ht, weight)
    #         weight_two = hash_table_retrieve(ht, limit - weight)
    #         for item in ht.storage:
    #             if item:
    #                 print(item.key, ': ', item.value)
    #         print((weight_one, weight_two))
    #         if weight_one <= weight_two:
    #             return (weight_one, weight_two)
    #         else:
    #             return (weight_two, weight_one)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
