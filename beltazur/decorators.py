class classproperty(object):

    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        return self.method(owner)
