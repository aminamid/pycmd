#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging import getLogger,basicConfig
logger = getLogger(__name__)

from functools import wraps

defaultcfg="""---
format: "%(asctime)s%(msecs).03d %(process)d %(thread)x %(levelname).4s;%(module)s(%(lineno)d/%(funcName)s) %(message)s"
datefmt: "%Y%m%d %H%M%S"
"""
import sys
import json
import yaml

class color:
    BLUE = '\033[1;34m'
    BLUEL = '\033[0;34m'
    GREEN = '\033[1;32m'
    GREENL = '\033[0;32m'
    CYAN = '\033[1;36m'
    CYANL = '\033[0;36m'
    RED = '\033[1;31m'
    REDL = '\033[0;31m'
    PURPLE = '\033[1;35m'
    PURPLEL = '\033[0;35m'
    YELLOW = '\033[1;33m'
    BROWN = '\033[0;33m'
    WHITE = '\033[1;37m'
    GRAYL = '\033[0;37m'
    GRAYD = '\033[1;30m'
    BLACK = '\033[0;30m'
    ENDC = '\033[0m'


class Style:
    @classmethod
    def color(self, x, case='default'):
        col = { 'enter':color.GREEN, 'retrn':color.BLUE, 'default':'' }
        return  '{1}{0}{2}'.format(x.__repr__(), col[case], color.ENDC )

    @classmethod
    def plain(self, x, case=None):
        return '{0}'.format(x.__repr__())

    @classmethod
    def pretty(self, x, case=None):
        import pp
        return pp.pprintf(x)
    


def traclog( f, modname, log_style ):
    style = getattr(Style, log_style)
    @wraps(f)
    def _f(*args, **kwargs):
        logger.debug("ENTER: {0}.{1}({2})".format(modname, f.__name__, style(kwargs, 'enter') if kwargs else style(args, 'enter')))
        result = f(*args, **kwargs)
        logger.debug("RETRN: {0}.{1} return {2}".format(modname, f.__name__, style(result, 'retrn')))
        return result
    return _f

def dictmerge(old, new):
    return dict([(k,v) for k,v in old.items()+new.items()])

def to_stderr(logcfg={'level': 30}):
    logcfg_dict = dictmerge(dictmerge(yaml.load(defaultcfg),logcfg), {'stream': sys.stderr}) 
    basicConfig(**logcfg_dict)

def to_file(logcfg={'level': 30}):
    logcfg_dict = dictmerge(dictmerge(yaml.load(defaultcfg),logcfg), {'stream': sys.stderr}) 
    basicConfig(**logcfg_dict)


