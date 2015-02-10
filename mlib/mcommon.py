import itertools

def concat( lsts ):
    return list(itertools.chain(*lsts))

def concat_dicts( dicts ):
    return dict( concat([ d.items() for d in dicts ]) )

from datetime import datetime as dt

def datetimestr():
    return dt.now().strftime("%Y%m%d%H%M%S")

