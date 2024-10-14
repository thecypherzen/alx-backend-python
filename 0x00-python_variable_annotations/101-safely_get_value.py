#!/usr/bin/env python3
"""More involved type annotations"""


from typing import Any, Mapping, Mapping, TypeVar, Union

Custom = TypeVar("T")


# using TypeVars
def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[Custom, None] = None) -> \
                     Union[Any, Custom]:
    """ A function that returns value at a key of a mapping
        if it exists or None otherwise
    """
    if key in dct:
        return dct[key]
    else:
        return default
