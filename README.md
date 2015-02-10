## Load direnv and apply .envrc

```
. 00_dot
direnv allow
```

## install python module to local

```
pip install -r requirements.txt
```


## 

./dopycmd.py | jq '.[] | {name, slug}'

## TODO

* log to file

## Digitalocean

./dopycmd.py do_tmp_centos64 '{subcmd: new_droplet, parms: { name: host1 } }'
./dopycmd.py '{subcmd: destroy_droplet, parms: { droplet_id: 4099539 }}'
./dopycmd.py cmd/droplets  | jq '.[] | { name, id, networks } '
./dopycmd.py do_tmp_centos64 '{subcmd: new_droplet, parms: { name: host2 } }'


