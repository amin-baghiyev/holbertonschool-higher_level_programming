#!/usr/bin/python3
"""
This is the "add_integer" module.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    
    Args:
        a: The first number (int or float).
        b: The second number (int or float, defaults to 98).
    
    Returns:
        The integer addition of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (math.isinf(a) or math.isnan(a)):
        raise OverflowError("cannot convert float NaN or infinity to integer")
    if isinstance(b, float) and (math.isinf(b) or math.isnan(b)):
        raise OverflowError("cannot convert float NaN or infinity to integer")
    return (int(a) + int(b))
