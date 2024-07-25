# Requirements

# 2 inputs, digit, positive
# 1 function, sqrt(a**2 +b**2)
# 1 output, float, positive
# no external library
# sqrt function: positive number -> float

def hypot(a,b):
    """_summary_

    Args:
        a (_digit_): one side of right angle triangle (not hypotenuse)
        b (_digit_): different side of right angle triangle (not hypotenuse)

    Returns:
        _float_: hypotenuse of right angle triangle
    """
    return (a**2 + b**2)**0.5

def sqrt(a):
    return a**0.5

def abs(a):
    return (a**2)**0.5

print(hypot(3,4)/hypot(3,6))