# -*- coding: utf-8 -*-
# Copyright (c) 2010 Zooko Wilcox-O'Hearn
#  This file is part of pyutil; see README.rst for licensing terms.

# We require simplejson>= 2.1.0 and set its default behavior to
# use_decimal=True. This retains backwards compatibility with previous
# versions of jsonutil (although it means jsonutil now requires a recent
# version of simplejson).

# http://code.google.com/p/simplejson/issues/detail?id=34

import sys
from functools import partial, wraps
from itertools import izip, imap

import simplejson

__FUNCS = ('dumps', 'loads', 'dump', 'load')

setattr(sys.modules[__name__], '__doc__', simplejson.__doc__)

for (name, func) in izip(__FUNCS,
                         imap(partial(getattr, simplejson), __FUNCS)):
    setattr(sys.modules[__name__], name,
            wraps(func)(partial(func, use_decimal=True)))
