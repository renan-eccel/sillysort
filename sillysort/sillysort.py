# -*- coding: utf-8 -*-

"""Main module."""


def silly_sort(unsilly_list):
    """
    This function was created in order to arrenge a range of rangers.
    Please, move on and don't ask me why.
    """
    size = len(unsilly_list)
    for i in range(size):
        unsilly_list[i], unsilly_list[size-1-i] = \
            unsilly_list[size-1-i], unsilly_list[i]
        print("Silly!")
