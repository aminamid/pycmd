echo "## `date`"
echo
echo "### only slugs"
echo
echo \`\`\`
./dopycmd.py cmd/regions | jq '.[].slug'
echo \`\`\`
echo
echo \`\`\`
./dopycmd.py cmd/sizes | jq '.[].slug'
echo \`\`\`
echo
echo \`\`\`
./dopycmd.py cmd/images | jq '.[].slug'
echo \`\`\`
echo
echo "### regions"
echo
echo \`\`\`json
./dopycmd.py cmd/regions | jq '.'
echo \`\`\`
echo
echo "### sizes"
echo
echo \`\`\`json
./dopycmd.py cmd/sizes | jq '.'
echo \`\`\`
echo
echo "### images"
echo
echo \`\`\`json
./dopycmd.py cmd/images | jq '.'
echo \`\`\`
