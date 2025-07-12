def sort(width, height, length, mass) -> str:
    # checking invalid types
    if not all(isinstance(x, (int, float)) for x in (width, height, length, mass)):
        raise TypeError("All inputs must be int or float")

    # checking invalid values
    if any(x <= 0 for x in (width, height, length)) or mass < 0:
        raise ValueError("Dimensions must be > 0 and mass must be >= 0")

    volume = width * height * length

    # rules
    is_heavy = mass >= 20
    is_bulky = False
    if volume >= 1_000_000:
        is_bulky = True
    elif max([width, height, length]) >= 150:
        is_bulky = True

    # sorting
    if is_heavy and is_bulky:
        return 'REJECTED'
    elif is_heavy or is_bulky:
        return 'SPECIAL'

    return 'STANDARD'
