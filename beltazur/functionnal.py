def filter_function(function):
    """Decorates a function so that it becomes a specialized filter"""
    def _inner(iterable):
        return filter(function, iterable)
    return _inner


def map_function(function):
    """Decorates a function so that it becomes a specialized map"""
    def _inner(iterable):
        return map(function, iterable)
    return _inner


def compose(functions):
    """Compose the given fonction together, in the given order"""
    def _inner(*args):
        for f in functions:
            args = f(*args)
        return args
    return _inner
