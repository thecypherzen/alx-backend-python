#!/usr/bin/env python3
"""Duck-typing annotations"""


from typing import Any, Sequence, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first element of list if list or None"""
    if lst:
        return lst[0]
    else:
        return None
