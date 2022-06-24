from .array import Array
from .array import Array
from .stack import Stack
from .dictionary import Dictionary


def dictionary(initial_list: list = None, /) -> Dictionary:
    """Create a new instance of arraylab.Dictionary

    Args:
        initial_list (list, optional): The same argument as in arraylab.Dictionary.__init__. Defaults to None.

    Returns:
        Dictionary: The instantiated arraylab.Dictionary.
    """
    return Dictionary(initial_list)


def array(initial_list: list = None, /) -> Array:
    """Create a new instance of arraylab.Array

    Args:
        initial_list (list, optional): The same argument as in arraylab.Array.__init__. Defaults to None.

    Returns:
        Array: The instantiated arraylab.Array.
    """
    return Array(initial_list)


def stack(initial_list: list = None, /) -> Stack:
    """Create a new instance of arraylab.Stack

    Args:
        initial_list (list, optional): The same argument as in arraylab.Stack.__init__. Defaults to None.

    Returns:
        Stack: The instantiated arraylab.Stack.
    """
    return Stack(initial_list)
