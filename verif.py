
def is_valid_choice(choice,minimum,maximum):
    validator = [
        lambda x: x.isdecimal(), 
        lambda x: minimum <= int(x) <= maximum,
    ]
    result = all(condition(choice) for condition in validator)
    return result

