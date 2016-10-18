class FunctionDict(dict):

    def decorate(self, name):
        def decorator(function):
            self[name] = function
            return function
        return decorator

    def __call__(self, name, *args, **kwargs):
        return self[name](*args, **kwargs)
