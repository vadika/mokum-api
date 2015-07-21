# -*- coding: utf-8 -*-
__author__ = 'vadikas'

import urllib
from pprint import pprint
from datetime import datetime
import json
from bs4 import BeautifulSoup
import http.cookiejar
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError, HTTPError
import socket


class mokum:
    auth_token=""
    loginurl='https://mokum.ru/users/sign_in'
    posturl='https://mokim.ru/index.html'

    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    def __init__(self):
        csrf= urllib.request.Request(self.loginurl)
        ret=self.opener.open(csrf)

        soup=BeautifulSoup(ret.read().decode('utf8', 'ignore')
            ,"html.parser")
        for tags in soup.findAll("meta", {'name': 'csrf-token'}):
            self.auth_token = tags['content']


    def login(self, username, remote_key):
        failcode=True
        details = urllib.parse.urlencode({ 'utf8': '✓',
                                               'user[email]': username,
                                               'user[password]': remote_key,
                                               "user[remember_me]":"0",
                                               "authenticity_token":self.auth_token,
                                               "commit":"Log in",
                                               })
        details = details.encode('utf8')
        try:
            url = urllib.request.Request(self.loginurl, details)
            url.add_header("Referer",self.loginurl)

            responsedata=self.opener.open(url)

        except HTTPError as e:
            print("fail with %d"%e.code)


        if responsedata.geturl()!="https://mokum.ru/":
            failcode=False

        response=responsedata.read().decode('utf8', 'ignore')
        return failcode

    def post(self, posttext):
        postid=0
        return postid


    def comment(self, commenttext, postid):
        commentid=0
        return commentid


m = mokum()

if m.login("vadikas@gmail.com", "abanamat")==True:
    print ("logged in")
else:
    print ("not logged in")

id=m.post("Robots.txt = Роботз дот ти экс ти")
print ("post id=",id)