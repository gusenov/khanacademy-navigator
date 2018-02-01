Печать только N первых уровней монструозного JSON файла:

```bash
$ jq --raw-output 'reduce path(.[]?[]?[]?) as $path (.; setpath($path; {}))' "topictree.json" > "collapsed-3 topictree.json"
```

Выборка материалов по математике:

```bash
$ jq --raw-output --compact-output '.children[] | select(.title == "Math")' "topictree.json" > "Math topictree.json"
$ jq --raw-output --compact-output '.children[] | select(.title == "Math")' "Topics only.json" > "Math Topics only.json"
$ jq --raw-output --compact-output '.children[] | select(.title == "Math")' "Topics and Exercises.json" > "Math Topics and Exercises.json"
```
