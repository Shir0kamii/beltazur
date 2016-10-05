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
