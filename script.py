#!/usr/bin/python3
import os, json, shutil, time
import twint
from mastodon import Mastodon
from config import *

delim = chr(31)
mastodon = Mastodon(
    access_token = 'user.secret',
    api_base_url = url
    )

with open("last.txt", "r") as last:
    last = last.read().splitlines()

def scrape(user):
    c = twint.Config()
    c.Username = user
    c.Limit = 10
    c.Store_json = True
    c.Output = "now.json"
    c.Hide_output = True
    twint.run.Search(c)

def loader(fn):
    tlist = []
    with open(fn) as data:
        data = data.read().splitlines()
    for d in data:
        tlist.append(json.loads(d))
    tlist = delim.join([t["tweet"] for t in tlist])
    with open("now.txt", "w") as now:
        now.write(tlist)

def findnew():
    with open("last.txt") as last:
        last = last.read().split(delim)
    with open("now.txt") as now:
        now = now.read().split(delim)
    diff = list(set(now).difference(last))
    return diff


def main():
    scrape(twitter)
    loader("now.json")
    diff = findnew()
    if len(diff):
        for d in diff:
            mastodon.toot(d)
            time.sleep(5)
        shutil.copy("now.txt", "last.txt")

