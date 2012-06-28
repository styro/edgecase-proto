#!/usr/bin/python

import itertools
import xml.etree.ElementTree as etree

def parse_links(filename):
    tree = etree.parse(filename)
    posts = tree.findall('post')
    return [post.attrib for post in posts]
