#!/usr/bin/env python
# encoding: utf-8

import time, os
from django.conf import settings


def file_iterator(file_name, chunk_size=512):
    with open(file_name, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def file_upload(file, url):
    file_name = str(file)
    name = str(file_name).split('.')
    t = time.time()
    file_name = str(int(t)) + '.' + name[1]
    file_dir = settings.MEDIA_ROOT + '/' + url + '/'
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file_path = file_dir + file_name
    file_relative_path = settings.MEDIA_URL + url + '/' + file_name
    open(file_path, 'wb+').write(file.read())

    return [str(file), file_relative_path]
