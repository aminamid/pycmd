#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import yaml
import inspect
from functools import reduce

from mlib import mlog
from mlib import mcmd
from mlib.mcommon import concat_dicts, datetimestr
from dopy.manager import DoManager


defaultcfg="""---
mlog:
  enabled: true
  basicconfig:
    level: 10
  patch:
    enabled: true
    style: color # plain | color | pretty
    targets:
    - [DoManager]
    - [json]
dopy:
  client_id: None
  api_key: "apikey"
  api_version: 2
"""
def loggify(objlist, wrapper, log_style):
    target = reduce( getattr,  [globals()[objlist[0]]] + objlist[1:] )
    attrs = [ a for (a,b) in inspect.getmembers(target) if inspect.ismethod(b) or inspect.isfunction(b) ]
    if not attrs:
        target = wrapper(target,target.__name__, log_style)
    else:
        for attr in attrs:
            setattr(target, attr, wrapper(getattr(target, attr),target.__name__, log_style))

def logconfigure(cfg):
    mlogcfg = cfg['mlog']
    if not ('enabled',True) in mlogcfg.items(): return
    mlog.to_stderr(mlogcfg['basicconfig'])

    if not ('enabled',True) in mlogcfg['patch'].items(): return
    for objlist in mlogcfg['patch']['targets']:
        loggify( objlist, mlog.traclog,  mlogcfg['patch']['style'] )

def main(cfg):
    do = DoManager(**cfg['dopy'])
    if cfg['subcmd'] in ['all_regions', 'all_images', 'sizes', 'all_active_droplets','all_domains', 'all_actions', 'all_ssh_keys']:
        method = getattr(do, cfg['subcmd'])
        return method()
    if cfg['subcmd'] in ['new_droplet']:
        method = getattr(do, cfg['subcmd'])
        result = method(**concat_dicts([cfg['new_droplet_template'], cfg['parms']] ))
        return result
    if cfg['subcmd'] in ['destroy_droplet']:
        method = getattr(do, cfg['subcmd'])
        return method(**cfg['parms'])


if __name__=='__main__':

    import os
    import sys
 
    mname = os.path.splitext(__file__)[0]
    defaultcfgfile =  '{0}.cfg'.format(mname) 

    cfg = mcmd.get_cfgdict( [ defaultcfg , defaultcfgfile ] + sys.argv[1:])
    logconfigure(cfg)
    mcmd.put_dict( 'tmp/{0}.cfg.dump'.format(mname), cfg, yaml.dump )
    result = main(cfg)
    print json.dumps(result)
    mcmd.put_dict( 'tmp/{0}.stat.{1}'.format(mname,datetimestr() ), result, json.dumps )
    
