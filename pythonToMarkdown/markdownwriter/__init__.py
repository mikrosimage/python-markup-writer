# outer __init__.py
try:  # python2
    from MarkdownWriter import *
except ImportError:  # python3
    pass
