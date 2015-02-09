echo regions
./dopycmd.py cmd/regions | jq '.[].slug'

echo sizes
./dopycmd.py cmd/sizes | jq '.[].slug'

echo images
./dopycmd.py cmd/images | jq '.[].slug'

echo droplets
./dopycmd.py cmd/droplets | jq '.[].slug'
