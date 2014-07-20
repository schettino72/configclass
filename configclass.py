
# configclass

# The MIT License
# Copyright (c) 2014 Eduardo Naufel Schettino
# See LICENSE for details


import copy

from mergedict import ConfigDict


class ConfigMixin(object):
    """A dict with a `make()` to easy the creation with derived values.

    New items can not be added to dict after its creation.
    """
    def __setitem__(self, key, value):
        """make sure new items are not added after initialization"""
        if key not in self:
            msg = 'New items can not be added to Config, invalid key:{}'
            raise KeyError(msg.format(key))
        super(ConfigMixin, self).__setitem__(key, value)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, dict.__repr__(self))

    # http://stackoverflow.com/questions/2060972
    # subclassing-python-dictionary-to-override-setitem
    def update(self, *args, **kwargs):
        """overwrite `update` method so custom `__setitem__` is called"""
        if args:
            if len(args) > 1:
                raise TypeError("update expected at most 1 arguments, "
                                "got %d" % len(args))
            other = dict(args[0])
            for key in other:
                self[key] = other[key]
        for key in kwargs:
            self[key] = kwargs[key]

    def setdefault(self, key, value=None):
        """overwrite `setdefault` method so custom `__setitem__` is called"""
        if key not in self:
            self[key] = value
        return self[key]
    # end - redefinition of methods to make sure __setitem__ is always called

    def copy(self):
        """copy that returns a Config object instead of plain dict"""
        return self.__class__(self)

    def as_dict(self):
        """return config as plain dict"""
        return dict(self)

    # implement magic methods used on `copy` module
    __copy__ = copy

    def __deepcopy__(self, memo):
        return self.__class__(copy.deepcopy(self.as_dict(), memo))


    # non-dict methods
    def make(self, *args, **kwargs):
        """Returns a new Config object, updating with given values.

        Arguments are same as dict.update().

        Also accepts None as single argument, in this case just return a copy
        of self.
        """
        result = copy.deepcopy(self)
        if not(args and args[0] is None):
            result.update(*args, **kwargs)
        return result



class Config(ConfigMixin, ConfigDict):
    # overwrite to use ConfigDict.merge() instead of update
    def make(self, *args, **kwargs):
        """Returns a new Config object, updating with given values.

        Arguments are same as dict.update().

        Also accepts None as single argument, in this case just return a copy
        of self.
        """
        result = copy.deepcopy(self)
        if not(args and args[0] is None):
            result.merge(*args, **kwargs)
        return result

