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

def interfaces():
    return [ traclogs ]

def traclog( f ):
    @wraps(f)
    def _f(*args, **kwargs):
        logger.info("ENTER: {0}({1})".format(f.__name__, json.dumps(kwargs) ))
        result = f(*args, **kwargs)
        logger.info("RETRN: {0} return {1}".format(f.__name__, json.dumps(result) ))
        return result
    return _f

def traclogpp( f ):
    import pp
    @wraps(f)
    def _f(*args, **kwargs):
        logger.info("ENTER: {0}({1})".format(f.__name__, pp.pprintf(kwargs) ))
        result = f(*args, **kwargs)
        logger.info("RETRN: {0} return {1}".format(f.__name__, pp.pprintf(result) ))
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


