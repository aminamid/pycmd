#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import yaml

from mlib import mlog
from mlib import mcmd
from dopy.manager import DoManager


defaultcfg="""---
logenabled: true
logging:
  level: 10
log_trac:
  DoManager: [__init__, all_regions, all_images, sizes, all_active_droplets, droplet_v2_action, show_all_actions, all_domains]
dopy:
  client_id: None
  api_key: "apikey"
  api_version: 2
"""

def logconfigure(cfg):
    if not cfg['logenabled']: return
    mlog.to_stderr(cfg['logging'])
    for k,v in cfg['log_trac'].items():
        cls = globals()[k]
        for func in v:
            if cfg['logpp']:
                setattr(cls, func, mlog.traclogpp(getattr(cls, func)))
            else:
                setattr(cls, func, mlog.traclog(getattr(cls, func)))

def main(cfg):
    do = DoManager(**cfg['dopy'])
    if cfg['subcmd'] in ['all_regions', 'all_images', 'sizes', 'all_active_droplets','all_domains', 'show_all_actions']:
        method = getattr(do, cfg['subcmd'])
        return method()


if __name__=='__main__':

    import os
    import sys
 
    mname = os.path.splitext(__file__)[0]
    defaultcfgfile =  '{0}.cfg'.format(mname) 

    cfg = mcmd.get_cfgdict( [ defaultcfg , defaultcfgfile ] + sys.argv[1:])
    logconfigure(cfg)

    print json.dumps(main(cfg))
