#! /usr/bin/env python
import os
import shutil
import tempfile

from distutils.dir_util import mkpath


class cd(object):

    """Context that changes to a new directory.

    Examples
    --------
    >>> import os, tempfile
    >>> from landlab.testing.tools import cd

    Create a temporary directory for testing.

    >>> test_dir = os.path.realpath(tempfile.mkdtemp())

    Withing the context, we're in the new working directory, after exiting
    the context we're back where we started.

    >>> this_dir = os.getcwd()
    >>> with cd(test_dir) as _:
    ...     wdir = os.getcwd()
    >>> test_dir == wdir
    True
    >>> os.getcwd() == this_dir
    True

    If the new working directory does not exists, create it.

    >>> new_dir = os.path.join(test_dir, 'testing.d')
    >>> os.path.exists(new_dir)
    False
    >>> with cd(new_dir) as _:
    ...     wdir = os.getcwd()
    >>> os.path.exists(new_dir)
    True
    >>> wdir == new_dir
    True
    >>> os.getcwd() == this_dir
    True
    """

    def __init__(self, path_to_dir):
        self._dir = path_to_dir

    def __enter__(self):
        self._starting_dir = os.path.abspath(os.getcwd())
        if not os.path.isdir(self._dir):
            mkpath(self._dir)
        os.chdir(self._dir)
        return os.path.abspath(os.getcwd())

    def __exit__(self, ex_type, ex_value, traceback):
        os.chdir(self._starting_dir)


class cdtemp(object):

    """Context that creates and changes to a temporary directory.

    Examples
    --------
    >>> import os
    >>> from landlab.testing.tools import cdtemp

    Change to the newly-created temporary directory after entering the
    context. Upon exiting, remove the temporary directory and return to the
    original working directory.

    >>> this_dir = os.getcwd()
    >>> with cdtemp() as tdir:
    ...     wdir = os.getcwd()
    >>> this_dir == os.getcwd()
    True
    >>> os.path.exists(wdir)
    False
    """

    def __init__(self, **kwds):
        self._kwds = kwds
        self._tmp_dir = None

    def __enter__(self):
        self._starting_dir = os.path.abspath(os.getcwd())
        self._tmp_dir = tempfile.mkdtemp(**self._kwds)
        os.chdir(self._tmp_dir)
        return os.path.abspath(self._tmp_dir)

    def __exit__(self, ex_type, ex_value, traceback):
        os.chdir(self._starting_dir)
        shutil.rmtree(self._tmp_dir)


def _reset_env(keep=None, env=None):
    """Reset the current environmt.

    Parameters
    ----------
    keep : list of str
        Names of environment variables to keep.
    env : dict
        Environment variable names/values for the new environment.
    """
    keep = keep or set()

    for key in os.environ.keys():
        if key not in keep:
            del os.environ[key]

    if env is not None:
        os.environ.update(env)



class setenv(object):

    """Context that sets up a new environment."""

    def __init__(self, env):
        self._env = env

    def __enter__(self):
        self._starting_env = os.environ.copy()
        _reset_env(env=self._env)

    def __exit__(self, type, value, traceback):
        _reset_env(env=self._starting_env)
