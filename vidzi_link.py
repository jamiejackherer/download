#!/usr/bin/python3
#-*- coding:utf-8 -*

import requests
import re
from bs4 import BeautifulSoup as bs
import jsbeautifier

def vidzi_link(vidzi_url):
    url = vidzi_url

    r = requests.get(url)
    s = bs(r.text, 'lxml')

    scripts = s.find_all('script', attrs={'type': 'text/javascript'})
    for x in scripts:
        if re.match(r"^(eval\(function\()(.)+(flash)*(.split\(\'\|\'\)\)\))$", x.text):
            obf_script = x.text

    deobf_script = jsbeautifier.beautify(obf_script)
    link = re.search(r'(http(s?):\/\/)([0-9])(.)+[a-z0-9]\.*(?:mp4)', deobf_script)

    return link.string[link.start():link.end()]

def vidzi_title(vidzi_url):

    url = vidzi_url

    r = requests.get(url)
    s = bs(r.text, 'lxml')
    title = s.find('h2', attrs={'class': 'video-title'})
    return title.text.replace('\n', '')\
                     .replace(' ', '')\
                     .replace('HDTV', '')\
                     .replace('x264', '')\
                     .replace('-', '')\
                     .replace('FLEET', '')\
                     .replace('AVS', '')\
                     .replace('KILLERS','')\
                     .replace('PROPER', '')\
                     .replace('ASAP', '')\
                     .replace('hdtv', '')\
                     .replace('AAC', '')\
                     .replace('WEBDL', '')\
                     .replace('lol', '')\
                     .replace('LOL', '')

