from typing import List, Union


def flatten_list(lst: List[Union[List, int ]]) -> List[int]:
    if not lst:
        return lst
    result = []
    for element in lst:
        if isinstance(element, int):
            result.append(element)
        else:
            result += flatten_list(element)
    return result


example = [1, [2, [3, 4]], 5, [6, 7], 8, [9, [10]]]

print(flatten_list(example))
