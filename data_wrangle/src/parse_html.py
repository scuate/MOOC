#!/usr/bin/env python
# -*- coding: utf-8 -*-
# parse html file

from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    """build a list where all the items are dictionaries containing the relevant data
    from each row in each file, skip the rows that contain the TOTAL data for a year. Output example:
    data = [{"courier": "FL",
            "airport": "ATL",
            "year": 2012,
            "month": 12,
            "flights": {"domestic": 100,
                        "international": 100}
            },
            {"courier": "..."}
    ]
    """
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")
    
    with open("{}/{}".format(datadir, f), "r") as html:
        soup = BeautifulSoup(html)
        info_lst = soup.find_all("tr", class_="dataTDRight")
        for i in info_lst:
            inf = i.find_all("td")
            if inf[1].text!="TOTAL":
                info['year'] = int(inf[0].text)
                info['month'] = int(inf[1].text) 
                info['flights']={'domestic':int(inf[2].text.replace(",","")), 'international':int(inf[3].text.replace(",",""))}
                data.append(info)        
    return data


def test():
    print "Running a simple test..."
    open_zip(datadir)
    files = process_all(datadir)
    data = []
    for f in files:
        data += process_file(f)
    
    assert len(data) == 399  # Total number of rows
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    print "... success!"

if __name__ == "__main__":
    test()