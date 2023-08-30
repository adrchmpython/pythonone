def calculation (initial_value, percentage, years):
    result = initial_value * (1 + percentage/100) ** years
    return result