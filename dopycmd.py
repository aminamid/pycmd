#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import yaml
import inspect
import functools

from mlib import mlog
from mlib import mcmd
from dopy.manager import DoManager


defaultcfg="""---
logenabled: true
logging:
  level: 10
log_targets:
  - [DoManager]
  - [json]
dopy:
  client_id: None
  api_key: "apikey"
  api_version: 2
log_style: color # plain | color | pretty
"""
def loggify(objlist, wrapper, log_style):
    target = functools.reduce( getattr,  [globals()[objlist[0]]] + objlist[1:] )
    attrs = [ a for (a,b) in inspect.getmembers(target) if inspect.ismethod(b) or inspect.isfunction(b) ]
    if not attrs:
        target = wrapper(target,target.__name__, log_style)
    else:
        for attr in attrs:
            setattr(target, attr, wrapper(getattr(target, attr),target.__name__, log_style))

def logconfigure(cfg):
    if not ('logenabled',True) in cfg.items(): return
    if not 'log_targets' in cfg: return
    mlog.to_stderr(cfg['logging'])
    for objlist in cfg['log_targets']:
        loggify( objlist, mlog.traclog,  cfg['log_style'] )

def main(cfg):
    do = DoManager(**cfg['dopy'])
    if cfg['subcmd'] in ['all_regions', 'all_images', 'sizes', 'all_active_droplets','all_domains', 'all_actions']:
        method = getattr(do, cfg['subcmd'])
        return method()


if __name__=='__main__':

    import os
    import sys
 
    mname = os.path.splitext(__file__)[0]
    defaultcfgfile =  '{0}.cfg'.format(mname) 

    cfg = mcmd.get_cfgdict( [ defaultcfg , defaultcfgfile ] + sys.argv[1:])
    logconfigure(cfg)
    mcmd.put_cfgdict( 'tmp/{0}.dump'.format(mname), cfg, yaml.dump )
    print json.dumps(main(cfg))
