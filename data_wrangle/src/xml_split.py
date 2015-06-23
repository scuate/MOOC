#!/usr/bin/env python
# -*- coding: utf-8 -*-
# split one xml file into several where the xml declaration should be the split point

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    with open(filename, 'r') as f:
        n = 0
        for line in f:
            
            if line.startswith('<?xml'):
                fw = open("{}-{}".format(filename, n), 'w')
                n += 1
            fw.write(line)


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()
