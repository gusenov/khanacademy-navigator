Печать только N первых уровней монструозного JSON файла:

```bash
$ jq --raw-output 'reduce path(.[]?[]?[]?) as $path (.; setpath($path; {}))' "topictree.json" > "collapsed-3 topictree.json"
```
