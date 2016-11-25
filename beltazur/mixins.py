class instanceproperty(object):

    def __init__(self, method):
        self.method = method


class InstancePropertyMixin(object):
    
    def __getattribute__(self, name):
        obj = object.__getattribute__(self, name)
        if isinstance(obj, instanceproperty):
            return obj.method(self)
        return obj

    def add_instance_property(self, name, method):
        setattr(self, name, instanceproperty(method))
