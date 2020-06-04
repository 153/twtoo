#!/usr/bin/python3
from mastodon import Mastodon
import * from config

def register():
    Mastodon.create_app(
        'tweet2masto',
        api_base_url = url,
        to_file = 'client.secret'
    )

try:
    with open("client.secret", "r") as cs:
        cs = cs.read()
        if len(cs) < 5:
            register()
except:
        register()
    
mastodon = Mastodon(
    client_id = 'client.secret',
    api_base_url = url,
)

def login(user, passw):
    mastodon.log_in(
        user, passw,
        to_file = "user.secret"
    )

try:
    with open("user.secret", "r") as us:
        us = us.read()
        if len(us) < 5:
            login(user, pw)
except:
    login(user, pw)

