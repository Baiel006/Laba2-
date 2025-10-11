def chain_powers(*args):
    if not args:
        return []
    result = [args[0] ** 1]
    for prev, current in zip(args, args[1:]):
        result.append(current ** prev)
    return result
