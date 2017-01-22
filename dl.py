#!/usr/bin/python3
#-*- coding:utf-8 -*-

import wget

def download_file(url, name):
    filename = name + '.mp4'
    filename = wget.download(url, out=filename)
    return
