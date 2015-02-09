#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json
import yaml
from logging import basicConfig

from mlib import mlog
from dopy.manager import DoManager


class CfgMustBeDict(Exception):
    def __init__(self, text):
        self._text = text
    def __str__(self):
        return 'Configuration element must be dict: {0}'.format(self._text)


def parse( st ):
    if str_to_dict(_try_open( st )): return str_to_dict(_try_open( st ))
    if _try_json(st): return _try_json(st)
    if _try_yaml(st): return _try_yaml(st)
    return None

def str_to_dict( st ):
    if not st: return None
    if _try_json(st): return _try_json(st)
    if _try_yaml(st): return _try_yaml(st)
    return None

def _try_yaml( st ):
    try:
        rslt = yaml.load(st)
        if isinstance(rslt, (dict)):
            return rslt
        else:
            raise CfgMustBeDict(st)
    except yaml.scanner.ScannerError as e:
        return None
    return None

def _try_json( st ):
    try:
        rslt = json.loads(st)
        if isinstance(rslt, (dict)):
            return rslt
        else:
            raise CfgMustBeDict(st)
    except ValueError as e:
        return None
    return None

def _try_open( st ):
    import codecs
    try:
        return codecs.open(st,'r', 'utf_8').read()
    except IOError as e:
        return None

def _concat( lsts ):
    from itertools import chain
    return list(chain(*lsts))

def _convert_to_dicts( cfg_list ):
    return map(parse, cfg_list)

def _dict_to_tuples( dicts ):
    return _concat([d.items() for d in dicts ])

def get_cfgdict( cfg_list ):
    return dict([(k,v) for k,v in _dict_to_tuples( _convert_to_dicts( cfg_list ))])

def put_cfgdict(st, cfg, encode):
    import codecs
    try:
        codecs.open(st, 'w', 'utf_8').write(encode(cfg))
    except IOError as e:
        return None
