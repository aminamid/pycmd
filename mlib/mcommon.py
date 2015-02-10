import itertools

def concat( lsts ):
    return list(itertools.chain(*lsts))

def concat_dicts( dicts ):
    return dict( concat([ d.items() for d in dicts ]) )

