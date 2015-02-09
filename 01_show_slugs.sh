echo "## `date`"
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
