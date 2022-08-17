#!/usr/bin/env python

# Copyright (c) 2022 Phumin Maliwan

"""
create by Phumin-DEV ( Phumin Maliwan )
This sourcecode may not be sold without permission. If violated, legal action will be taken to the maximum extent.
Follow me on social
    Github: https://github.com/mantvmass
    Facebook: https://facebook.com/PhuminMailwan
    YouTube: MOBILE MINING
"""

import requests

# url_replace = { "%7B": "{", "%7D": "}", "%2C": "," }
HOST_GRAPH = "https://graph.facebook.com/"


class GraphAPI(object):

    def __init__(self,access_token=None,) -> None:
        self.access_token = access_token

    def _payload(self, id, data) -> str:
        if data == "": signdata = "{}?access_token={}".format(id, self.access_token)
        else: signdata = "{}?fields={}&access_token={}".format(id, data, self.access_token)
        # print("payload: ", signdata)
        return str(signdata)

    def getcontent(self, id, data=""):
        result = requests.get(HOST_GRAPH + self._payload(id, data))
        return result.json()

