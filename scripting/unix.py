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


def wc_l(fname, with_wc='wc'):
    """Count the lines in a file.

    Parameters
    ----------
    fname : str
        File name.
    with_wc : str, optional
        The 'wc' command to use (default is `wc`).

    Returns
    -------
    int
        Number of lines in file, or None on error.

    """
    try:
        n_lines = subprocess.check_output(
            [with_wc, '-l', fname])
    except Exception:
        raise
    else:
        return int(n_lines.split()[0])


def tail(fname, n=10, with_tail='tail'):
    """Get the last lines in a file.

    Parameters
    ----------
    fname : str
        File name.
    n : int, optional
        Number of lines to get (default is 10).
    with_tail : str, optional
        The 'tail' command to use (default is `tail`).

    Returns
    -------
    str
        The last lines in file, or None on error.

    """
    fname = os.path.abspath(fname)
    try:
        lines = subprocess.check_output(
            [with_tail, '-n{n}'.format(n=n), fname])
    except subprocess.CalledProcessError:
        raise RuntimeError('Unable to get status. Please try again.')
    except Exception:
        raise
    else:
        return lines.strip()

