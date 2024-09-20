#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import numpy as np


def bubble_sort(values: list) -> list:
    """
    Description:
    ===========
    This function iterates over an array in ascending order,
    compares the elements in the array and swaps them.

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

    :param values: list: List of values
    :return: list
    """
    start_time = time.time()
    # print(values)
    number_of_elements = len(values)
    # Iterate in descending order, from the number_of_elements (last index) to 0, at of step -1
    for n in np.arange(number_of_elements - 1, 0, -1):
        # print(f"Descending pass index: {n}")
        # Iterate in ascending order, from 0 to n
        for i in range(n):
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
    # print(f"Duration: {time.time() - start_time}")
    return values


def bubble_sort_opt(values: list) -> list:
    """
    Description:
    ===========


    Notes:
    =====
    Sorting an array means to arrange the elements in the array in a certain order,
    either ascending or descending. In general terms, Ascending means smallest to
    largest, 0 to 9, and/or A to Z and Descending means largest to smallest, 9 to 0,
    and/or Z to A.

    :param values: list:
    :return: list
    """
    start_time = time.time()
    # print(values)
    number_of_elements = len(values)
    precious_value, index, next_value, swapped = 1, 1, 1, 1
    # Iterate in descending order, from the number_of_elements (last index) to 0, at of step -1
    for n in np.arange(number_of_elements - 1, 0, -1):
        # print(f"Descending pass index: {n}, Swapped: {swapped}")
        if swapped:
            swapped = 0
            # Iterate in ascending order, from 0 to n
            for i in range(n):
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
    # print(f"Duration: {time.time() - start_time}")
    return values


def bubble_sort_by_order_of_2(values: list) -> list:
    """
    Description:
    ===========


    Notes:
    =====
    Sorting an array means to arrange the elements in the array in a certain order,
    either ascending or descending. In general terms, Ascending means smallest to
    largest, 0 to 9, and/or A to Z and Descending means largest to smallest, 9 to 0,
    and/or Z to A.

    :param values: list:
    :return: list
    """
    start_time = time.time()
    # print(values)
    number_of_elements = len(values)
    # Iterate in descending order, from the number_of_elements (last index) to 0, at of step -1
    for n in np.arange(number_of_elements - 1, 0, -2):
        # print(f"Descending pass index: {n}")
        # Iterate in ascending order, from 0 to n
        for i in range(n):
            # print(f"Ascending pass index: {i}")
            if i % 2 != 0:
                # Compare the previous and next value
                if values[i] > values[i + 2]:
                    # swap elements
                    previous_value = values[i - 1: i + 1]
                    next_value = values[i + 1: i + 3]
                    # print(f"Previous Value: {previous_value}")
                    # print(f"Next value: {next_value}")
                    # assign the swapped values
                    values[i - 1: i + 1] = next_value
                    values[i + 1: i + 3] = previous_value
    # print(f"Duration: {time.time() - start_time}")
    return values


def create_nested_list(values: list) -> list:
    start_time = time.time()
    number_of_elements = len(values)
    nested_list = []
    # Iterate in descending order, from the number_of_elements (last index) to 0, at of step -1
    for n in range(0, number_of_elements, 2):
        # print(f"iteration: {n}")
        nested_list.append(values[n: n + 2])
    # print(f"Duration: {time.time() - start_time}")
    return nested_list

