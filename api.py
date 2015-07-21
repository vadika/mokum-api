# -*- coding: utf-8 -*-
__author__ = 'vadikas'

import urllib
from pprint import pprint
from datetime import datetime
import json
from bs4 import BeautifulSoup
import http.cookiejar
import urllib.request, urllib.parse, urllib.error
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
            auth_token = tags['content']

        print (auth_token)



    def login(self, username, remote_key):
       failcode=False
        try:
            details = urllib.parse.urlencode({ 'utf8': '✓',
                                               'user[email]': username,
                                               'user[password]': remote_key,
                                               "user[remember_me]":"1",
                                               "authenticity_token":auth_token,
                                               "commit":"Log in",
                                               })
            details = details.encode('UTF-8')

            url = urllib.request.Request(self.loginurl, details)
            url.add_header("Referer",self.loginurl)

            responsedata = self.opener.open(url)
            errcode=responsedata.getcode()
            print(responsedata.geturl())
            response=responsedata.read().decode('utf8', 'ignore')


        except urllib.error.HTTPError as e:
            responsedata = e.read().decode('utf8', 'ignore')
            failcode = False

        except urllib.error.URLError as e:
            print (e.code)
            failcode = True

        print(ascii(response))
        return failcode

    def post(self, posttext):
        postid=0
        return postid


    def comment(self, commenttext, postid):
        commentid=0
        return commentid

m = mokum()
m.login("vadikas@gmail.com", "abanamat")
