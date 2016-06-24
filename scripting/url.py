#! /usr/bin/env python
import os
import urllib2
import shutil


def download_url(url, dest, md5=None, cache='.'):
    dest = os.path.abspath(os.path.join(cache, dest))

    if os.path.exists(dest):
        if md5 and checksum(dest) == md5:
            return dest
        else:
            os.remove(dest)

    try:
        response = urllib2.urlopen(url)
    except urllib2.HTTPError as error:
        raise
    except urllib2.URLError as error:
        raise
    else:
        with open(dest, 'w') as destination:
            shutil.copyfileobj(response, destination)

    return os.path.abspath(dest)


