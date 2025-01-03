#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.utils.sort_algorithms import bubble_sort_by_order_of_2, create_nested_list

if __name__ == "__main__":
    # print(bubble_sort([5, 4, 3, 9, 8, 5, 7, 1]))
    sorted_list = bubble_sort_by_order_of_2(
        [
            "Harry",
            "37.21",
            "Berry",
            "37.21",
            "Tina",
            "37.2",
            "Akriti",
            "41",
            "Harsh",
            "39",
        ]
    )
    print(f"Sorted Values: \n{sorted_list}")
    # Output: ['Tina', '37.2', 'Harry', '37.21', 'Berry', '37.21', 'Harsh', '39', 'Akriti', '41']
    nested_list = create_nested_list(sorted_list)
    print(f"Nested List: {nested_list}")
