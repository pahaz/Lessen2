
__author__ = 'pahaz'


class cached_property(object):
    """
    Decorator that converts a method with a single
    self argument into a property cached on the instance.

    Optional ``name`` argument allows you to make cached properties
    of other methods.
    (e.g.  url = cached_property(get_absolute_url, name='url') )

    >>> class A:
    ...     @cached_property
    ...     def foo(self):
    ...         from random import randint
    ...         return randint(1, 100000)
    >>> a = A()
    >>> a.foo == a.foo
    True
    """
    def __init__(self, func, name=None):
        self.func = func
        self.__doc__ = getattr(func, '__doc__')
        self.name = name or func.__name__

    def __get__(self, instance, type=None):
        if instance is None:
            return self
        res = instance.__dict__[self.name] = self.func(instance)
        return res
