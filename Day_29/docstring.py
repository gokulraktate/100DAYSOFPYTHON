# Docstrings in Python | Python Tutorial - Day #29

# https://www.youtube.com/watch?v=SJzsNd7SM0g&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=29


def square(n):
    '''This takes in a number n, returns th square of n'''
    #the doc string is written just below the function name or just above the function body
    print(n**2)
square(5)

print(square.__doc__)


#Use of "import this"
# The Zen of Python

# PS D:\100DAYSOFPYTHON> python
# Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import this
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# >>>