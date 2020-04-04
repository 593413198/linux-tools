# linux-tools

**environment**
`linux + python3`

-----


## pySearch
Search file by given filename or path

```
usage: Search file by give filename or path
eg. pySearch -f .py -p .  [在当前目录下搜索.py后缀的文件]
    pySearch -f README.md -p doc/ [在doc/目录下搜索README.md文件]

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         display version information
  -f FILENAME, --filename FILENAME
                        target file to search
  -p PATH, --path PATH  target path to search
  --ignore              never care lower or upper case
  --relpath             show relative path
  --include             show partly same filename
```
