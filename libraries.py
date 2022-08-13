"""
Module contains best practices for build in libraries
"""

"""
1. Use pathlib instead of os.path

os.path module is a simple way to manipulate paths. Unfortunately all os.path's functions return strings.
It means that we have to use multiple nesting to get proper result.

Lets say we have some file on path:
/home/user/app/some_dir/some_file.txt

We would like to generate new path in some other directory to copy that file. Target should be:
/home/user/app/new_app/new_dir/some_file.txt

"""

# os.path examples
import os

some_path = '/home/user/app/some_dir/some_file.txt'

new_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(some_path)), 'new_dir'), 'some_file.txt')

# Pathlib example

from pathlib import Path

some_path = '/home/user/app/some_dir/some_file.txt'

new_path = Path(some_path).parent.parent / 'new_dir' / 'some_file.txt'

"""
Looks much better, does it not ?
It's possible as any manipulating path using Path object (going to parent dir, joining etc) return new Path object.

As we can see it also got __div__ implemented as we can use "/" to join paths.

Warning: if you print result you see '/home/user/app/new_dir/some_file.txt', but object is not a string, it's Path with
__str__ implemented. If you want string representation use as_posix() method or just str() casting.

Both libraries are built in.
"""


"""
2. Use argparse instead of sys.argv

sys.argv is simple function used to catch argument passed to file while running.

For example:
>>> python libraries.py arg_1 22 '{"foo": "bar"}'
"""
import sys
print(sys.argv)  # result: ['libraries.py', 'Neverland', '22', '{foo: bar}']
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])


"""
As we can see there are multiple issues with this solution:
1. Always the first argument is file name, we have to always remember that.
2. Arguments passed from terminal are always treated as strings and sys.arg doesn't have any casting mechanism built in.
3. We are not able to pass arguments as keyword (e.g. --country Neverland) in simple way \
    (without building some mechanism to parse it)
4. As all arguments are position we can easily make mistake replacing some of indexes.

Argparse provides us much better way to do it, solving all above issues. It may look a bit more difficult to code, \
    but provides us straight and clear way to parsing arguments.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--country')
parser.add_argument('--number')
parser.add_argument('--json')
args = parser.parse_args()

print(vars(args))  # {'country': 'Neverland', 'number': '22', 'json': '{"foo": "bar"}'}
print(args.country)  # Neverland

"""
Above code was run with keyword arguments what make it much more clear.
>>> python libraries.py --country Neverland --number 22 --json '{"foo": "bar"}'


Argparse provides us multiple optional parameters to be set up, like type for automatic casting.
Some of them use with our example:
"""
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--country', required=True, help='Your favorite country')
parser.add_argument('--number', type=int, required=True, help='Your favorite number')
parser.add_argument('--json', type=json.loads, help='Additional informations')
args = parser.parse_args()

print(vars(args))  # {'country': 'Neverland', 'number': 22, 'json': {'foo': 'bar'}}

"""
If we have 'help' parameters provided then it's a great documentation for developers.
In that case argparse also provide us information for file parameters:
>>> python libraries.py -h

///
usage: libraries.py [-h] --country COUNTRY --number NUMBER [--json JSON]

optional arguments:
  -h, --help         show this help message and exit
  --country COUNTRY  Your favorite country
  --number NUMBER    Your favorite number
  --json JSON        Additional informations
///

For further information check: https://docs.python.org/3/library/argparse.html
Both libraries (argparse and sys) are built in.
"""