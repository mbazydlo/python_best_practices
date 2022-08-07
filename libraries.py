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

# os.path exaples
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
2. Use decouple instead of os.environ

Decouple lib is 3th party, so we have in

"""