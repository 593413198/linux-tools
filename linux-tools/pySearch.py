#!/usr/bin/python3
# @brief: search target file in current directory
# @author: luhao
# @date: 2020,4,4

import argparse
import os

_version = "\033[1;32mpySearch v1.0 (c) 2020-2020 by luhao\33[0m"
_usage = """\33[1;32mSearch file by give filename or path\33[0m
eg. pySearch -f .py -p .  [在当前目录下搜索.py后缀的文件]
    pySearch -f README.md -p doc/ [在doc/目录下搜索README.md文件]
"""

parse = argparse.ArgumentParser(usage=_usage)
parse.add_argument('-V', '--version', help='display version information', action='store_true')
parse.add_argument('-f', '--filename', help='target file to search')
parse.add_argument('-p', '--path', help='target path to search', default='.')
parse.add_argument('--ignore', help='never care lower or upper case', default=False, action='store_true')
parse.add_argument('--relpath', help='show relative path', default=False, action='store_true')
parse.add_argument('--include', help='show partly same filename', default=False, action='store_true')
args = parse.parse_args()


def analyse():
    """
    :return: path of target file
    """
    if args.version:
        print(_version)
        return
    if not args.filename:
        print("\33[31mError: Please Enter FileName\n\33[0m");
        return
    filename = args.filename
    path = args.path

    # 判断是否是绝对路径
    if not os.path.isabs(path):
        path = os.getcwd() + '/' + path
    if path[-2:] == '/.':
        path = path[:-2]
    if args.ignore:
        print("Search \33[1;32m[%s(%s)]\33[0m in \33[1;32m%s\33[0m" % (filename, filename.lower(), path))
    else:
        print("Search \33[1;32m%s\33[0m in \33[1;32m%s\33[0m" % (filename, path))

    ans_include = []
    ans_equal = []
    # 遍历当前目录
    _filename = filename.lower() if args.ignore else filename
    for root, dirs, files in os.walk(path):
        for name in files:
            _name = name.lower() if args.ignore else name
            if _name == _filename:
                ans_equal.append(os.path.join(root, name))
            elif args.include and _filename in _name:
                ans_include.append(os.path.join(root, name))
    print("\33[1;34mPath (Totally Equal):\33[0m")
    for i in ans_equal:
        _i = os.path.relpath(i) if args.relpath else i
        print(_i)
    if args.include:
        print("\33[1;34mPath (Partly Equal):\33[0m")
        for i in ans_include:
            _i = os.path.relpath(i) if args.relpath else i
            print(_i)
    print("\33[1;34m%d files found\n\33[0m" % (len(ans_equal) + len(ans_include)))


if __name__ == '__main__':
    analyse()
