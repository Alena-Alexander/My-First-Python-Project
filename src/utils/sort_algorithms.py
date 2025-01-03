#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import numpy as np


def bubble_sort(values: list) -> list:
    """
    Description:
    ===========

    Bubble sort is a sorting algorithm that compares two adjacent elements
    and swaps them until they are in the intended order.

    Working of Bubble Sort:
    ======================

    Suppose we are trying to sort the elements in ascending order.

    1. First Iteration (Compare and Swap)

    1.2. Starting from the first index :math:`n`, compare the first and the second element
    at index :math:`n + 1`.

    2. If the first element is greater than the second element, they are swapped.

    3. Now, compare the second and the third elements. Swap them if they are not in order.

    4. The above process goes on until the last element.

    Pseudocode:
    ==========

    >>> bubbleSort(array)
    >>> for i <- 1 to sizeOfArray - 1
    >>>     for j <- 1 to sizeOfArray - 1 - i
    >>>         if leftElement > rightElement
    >>>             swap leftElement and rightElement
    >>> end bubbleSort


    Notes:
    =====

    Sorting an array means to arrange the elements in the array in a certain order,
    either ascending or descending. In general terms, Ascending means smallest to
    largest, 0 to 9, and/or A to Z and Descending means largest to smallest, 9 to 0,
    and/or Z to A.

    Example:
    =======

    >>> print(bubble_sort([5,8,2,5,4,8]))
    >>> [2,4,5,5,8,8]

    :param values: list: A collection of values.
    :return: list: a collection of sorted values
    """
    start_time = time.time()
    # print(values)
    number_of_elements = len(values)
    # Iterate in descending order, from the number_of_elements (last index) to 0, at of step -1
    for n in np.arange(start=number_of_elements - 1, stop=0, step=-1):  # <== direction
        # print(f"Descending pass index: {n}")
        # Iterate in ascending order, from 0 to n
        for i in np.arange(start=0, stop=n, step=1):  # ==> direction
            # print(f"Ascending pass index: {i}")
            # Compare the previous and next value
            if values[i] > values[i + 1]:
                # swap elements
                previous_value = values[i]
                next_value = values[i + 1]
                # print(f"Previous Value: {previous_value}")
                # print(f"Next value: {next_value}")
                # assign the swapped values
                values[i] = next_value
                values[i + 1] = previous_value
    print(f"Duration: {time.time() - start_time}")
    return values


def bubble_sort_opt(values: list) -> list:
    """
     Description:
    ===========

    Bubble sort optimized is a sorting algorithm that compares two adjacent elements
    and swaps them until they are in the intended order.

    Working of Bubble Sort:
    ======================

    Suppose we are trying to sort the elements in ascending order. In this
    optimized approach we can improve it by using one extra flag ``swapped``. No more
    swaps indicate the completion of sorting. If the list is already sorted,
    we can use this flag to skip the remaining passes

    1. First Iteration (Compare and Swap).

    1.2. Starting from the first index :math:`n`, compare the first and the second element
    at index :math:`n + 1`.

    2. If the first element is greater than the second element, they are swapped.

    3. Now, compare the second and the third elements. Swap them if they are not in order.

    4. The above process goes on until the last element.

    Notes:
    =====

    Sorting an array means to arrange the elements in the array in a certain order,
    either ascending or descending. In general terms, Ascending means smallest to
    largest, 0 to 9, and/or A to Z and Descending means largest to smallest, 9 to 0,
    and/or Z to A.

    Pseudocode:
    ==========

    >>> bubble_sort_opt(array)
    >>> flag = 1
    >>> for i <- 1 to sizeOfArray - 1
    >>>     if flag == 1:
    >>>         flag = 0
    >>>         for j <- 1 to sizeOfArray - 1 - i
    >>>             if leftElement > rightElement
    >>>                 swap leftElement and rightElement
    >>>                 flag = 1
    >>> end bubble_sort_opt


    Example:
    =======

    >>> print(bubble_sort_opt([5,8,2,5,4,8]))
    >>> [2,4,5,5,8,8]

    :param values: list: A collection of values.
    :return: list: : a collection of sorted values
    """
    start_time = time.time()
    # print(values)
    number_of_elements = len(values)
    swapped = 1
    # Iterate in descending order, from the number_of_elements (last index) to 0, at of step -1
    for index in np.arange(start=number_of_elements - 1, stop=0, step=-1):
        # print(f"Descending pass index: {n}, Swapped: {swapped}")
        if swapped:
            swapped = 0
            # Iterate in ascending order, from 0 to n
            for i in np.arange(start=0, stop=index, step=1):
                # print(f"Ascending pass index: {i}, if {values[i]} > {values[i + 1]} = {values[i] > values[i + 1]}")
                # Compare the previous and next value
                if values[i] > values[i + 1]:
                    # swap elements
                    previous_value = values[i]
                    next_value = values[i + 1]
                    # print(f"Previous Value: {previous_value}, Next value: {next_value}")
                    # assign the swapped values
                    values[i] = next_value
                    values[i + 1] = previous_value
                    swapped = 1
    print(f"Duration: {time.time() - start_time}")
    return values


def bubble_sort_by_order_of_2(values: list) -> list:
    """
     Description:
    ===========

    bubble_sort_by_order_of_2 is a sorting algorithm that compares two adjacent elements
    and swaps them until they are in the intended order.

    Working of Bubble Sort:
    ======================

    Suppose we are trying to sort the elements in ascending order.

    1. First Iteration (Compare and Swap).

    1.2. Starting from the first index :math:`n`, compare the first and the second element
    at index :math:`n + 2`.

    2. If the first element is greater than the second element, they are swapped.

    3. Now, compare the second and the third elements. Swap them if they are not in order.

    4. The above process goes on until the last element.

    Notes:
    =====

    Sorting an array means to arrange the elements in the array in a certain order,
    either ascending or descending. In general terms, Ascending means smallest to
    largest, 0 to 9, and/or A to Z and Descending means largest to smallest, 9 to 0,
    and/or Z to A.

    Example:
    =======

    >>> print(bubble_sort_by_order_of_2([5,8,2,5,4,8]))
    >>> [2,4,5,5,8,8]

    :param values: list: A collection of values.
    :return: list: a collection of sorted values
    """
    start_time = time.time()
    # print(values)
    number_of_elements = len(values)
    # Iterate in descending order, from the number_of_elements (last index) to 0, at of step -1
    for n in np.arange(number_of_elements - 1, 0, -2):
        # print(f"Descending pass index: {n}")
        # Iterate in ascending order, from 0 to n
        for i in np.arange(n):
            # print(f"Ascending pass index: {i}")
            if i % 2 != 0:
                # Compare the previous and next value
                if values[i] > values[i + 2]:
                    # swap elements
                    previous_value = values[i - 1 : i + 1]
                    next_value = values[i + 1 : i + 3]
                    # print(f"Previous Value: {previous_value}")
                    # print(f"Next value: {next_value}")
                    # assign the swapped values
                    values[i - 1 : i + 1] = next_value
                    values[i + 1 : i + 3] = previous_value
    print(f"Duration: {time.time() - start_time}")
    return values


def create_nested_list(values: list) -> list:
    start_time = time.time()
    number_of_elements = len(values)
    nested_list = []
    # Iterate in descending order, from the number_of_elements (last index) to 0, at of step -1
    for n in np.arange(start=0, stop=number_of_elements, step=2):
        # print(f"iteration: {n}")
        nested_list.append(values[n : n + 2])
    # print(f"Duration: {time.time() - start_time}")
    return nested_list


def num_of_identical_scores(sorted_list: list) -> int:
    sorted_list = bubble_sort_by_order_of_2(sorted_list)
    # It holds the value of the number of persons that have the same score,
    # we initialize it to 1, since at least one score will be the lowest.
    same_score_count = 1
    arr_length = len(sorted_list) - 2
    for i in range(arr_length):
        if (
            i % 2 == 1
        ):  # We use the number `2` because it represents how many elements identify a single person data.
            print(f"Index: {i} ==> comparing: {sorted_list[i]} & {sorted_list[i + 2]}")
            if sorted_list[i] == sorted_list[i + 2]:
                same_score_count += 1
    return same_score_count


if __name__ == "__main__":
    unsorted_values = [int(100 * a) for a in np.random.random(1000)]
    sorted_values1 = bubble_sort(unsorted_values.copy())
    # print(sorted_values1)
    sorted_values2 = bubble_sort_opt(unsorted_values.copy())
    # print(sorted_values2)
