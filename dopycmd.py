#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import yaml

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
    defaultcfgfile =  '{0}.cfg'.format(mname) if os.path.exists('{0}.cfg'.format(mname)) else None

    
    mlog.logconfigure(yaml.load('{enabled: true, basicconfig: {level: 10}, patch: {enabled: true, style: color, targets: [[mcmd]] } }'), lambda x: globals()[x])
    cfg = mcmd.get_cfgdict( [ defaultcfg , defaultcfgfile ] + sys.argv[1:])

    mlog.logconfigure(cfg['mlog'], lambda x: globals()[x])

    mcmd.put_dict( 'tmp/{0}.cfg.dump'.format(mname), cfg, yaml.dump )

    result = main(cfg)
    print json.dumps(result)

    mcmd.put_dict( 'tmp/{0}.stat.{1}'.format(mname,datetimestr() ), result, json.dumps )
    
