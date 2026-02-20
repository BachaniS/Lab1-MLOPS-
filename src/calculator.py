def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")

    return x + y


def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y


def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
    Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y


def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    """
    total_sum = x + y + z
    return total_sum


def profit_loss(cost_price, selling_price):
    """
    Calculates net profit or loss amount.
    Args:
        cost_price (int/float): Cost price of the item.
        selling_price (int/float): Selling price of the item.
    Returns:
        int/float: Net amount (positive = profit, negative = loss, zero = no change).
    Raises:
        ValueError: If inputs are not numbers.
    """
    if not (isinstance(cost_price, (int, float)) and isinstance(selling_price, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return selling_price - cost_price


def simple_interest(principal, rate, time):
    """
    Calculates simple interest.
    Args:
        principal (int/float): Principal amount.
        rate (int/float): Annual rate of interest (in percentage).
        time (int/float): Time period (in years).
    Returns:
        int/float: Simple interest amount.
    Raises:
        ValueError: If any input is not a number.
    """
    if not (
        isinstance(principal, (int, float))
        and isinstance(rate, (int, float))
        and isinstance(time, (int, float))
    ):
        raise ValueError("All inputs must be numbers.")
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time, compounds_per_year=1):
    """
    Calculates compound interest.
    Args:
        principal (int/float): Principal amount.
        rate (int/float): Annual rate of interest (in percentage).
        time (int/float): Time period (in years).
        compounds_per_year (int/float): Number of compounding periods per year.
    Returns:
        int/float: Compound interest amount.
    Raises:
        ValueError: If any input is not a number or if compounds_per_year is zero.
    """
    if not (
        isinstance(principal, (int, float))
        and isinstance(rate, (int, float))
        and isinstance(time, (int, float))
        and isinstance(compounds_per_year, (int, float))
    ):
        raise ValueError("All inputs must be numbers.")
    if compounds_per_year == 0:
        raise ValueError("compounds_per_year must not be zero.")

    amount = principal * (1 + (rate / (100 * compounds_per_year))) ** (compounds_per_year * time)
    return amount - principal
