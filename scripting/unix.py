#! /usr/bin/env python
import os
import subprocess
import platform


def is_linux():
    """Check if machine is linux."""
    return platform.system() == 'Linux'


def is_osx():
    """Check if machine is OSX."""
    return platform.system() == 'Darwin'


def is_unix():
    """Check if machine is either Linux or OSX."""
    return is_linux() or is_osx()


def is_executable(prog):
    """Check if a program is executable.

    Parameters
    ----------
    prog : str
        Name of the program to test.

    Returns
    -------
    bool
        True if the program is executable.

    """
    return os.path.isfile(prog) and os.access(prog, os.X_OK)


def which(prog, env=None):
    """Find path to a program.

    Parameters
    ----------
    prog : str
        Name of the program to search for.
    env : str
        Name of an environment variable that contains the program's path.
    """
    prog = os.environ.get(env or prog.upper(), prog)

    try:
        prog = subprocess.check_output(['which', prog],
                                       stderr=open('/dev/null', 'w')).strip()
    except subprocess.CalledProcessError:
        return None
    else:
        return prog


def checksum(path):
    import hashlib

    hasher = hashlib.md5()
    with open(path, 'r') as contents:
        hasher.update(contents.read())

    return hasher.hexdigest()


