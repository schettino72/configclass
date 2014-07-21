configclass - A Python to class to hold configuration values
==============================================================

.. display some badges

.. image:: https://travis-ci.org/schettino72/configclass.png?branch=master
  :target: https://travis-ci.org/schettino72/configclass

.. image:: https://coveralls.io/repos/schettino72/configclass/badge.png
        :target: https://coveralls.io/r/schettino72/configclass




A `Config` is a `dict` with a where:

 * existing items can be modified but no items can not be added
 * has `make()` method so you can easily created derived configs
 * `make()` has the same API as `dict.update()`
 * `make()` will merge values according to `mergedict.ConfigDict.merge()`
 * for convenience, make can take a `None` to perform a simple copy


::

    >>> from configclass import Config

    >>> c1 = Config({'a': 1, 'b': ['foo']})

    # can't add new items to config
    >>> c1.make({'a':2, 'c': [2]})
    Traceback (most recent call last):
    KeyError: 'New items can not be added to Config, invalid key:c'

    # new config object created
    >>> c2 = c1.make({'a':2})
    >>> c2
    Config({'a': 2, 'b': ['foo']})

    # original object is not modified
    >>> c1
    Config({'a': 1, 'b': ['foo']})

    # make() can take keyword arguments, note how lists are merged
    >>> c2.make(b=['bar'])
    Config({'a': 2, 'b': ['foo', 'bar']})



`configclass.ConfigMixin` can be used to create a `Config` class
that is not based on `mergedict.ConfigDict`.



Project Details
===============

- Project management on github - https://github.com/schettino72/configclass/


license
=======

The MIT License
Copyright (c) 2014 Eduardo Naufel Schettino

see LICENSE file


developers / contributors
==========================

- Eduardo Naufel Schettino


install
=======

::

 $ pip install configclass

or download and::

 $ python setup.py install


tests
=======

Install dependencies in `dev_requirements.txt`.

To run the tests::

  $ py.test

