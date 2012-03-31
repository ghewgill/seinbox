import json
import re
import urllib, urllib2
import zlib

with open("seinbox.app") as f:
    app = json.loads(f.read())

token = ""
try:
    with open("seinbox.token") as f:
        token = f.read().strip()
except IOError:
    pass

if not token:
    print "Go here in your browser:"
    print "https://stackexchange.com/oauth?client_id=%d&scope=read_inbox,no_expiry&redirect_uri=%s" % (app["client_id"], app["redirect_uri"])
    code = raw_input("code: ")
    r = urllib2.urlopen("https://stackexchange.com/oauth/access_token", urllib.urlencode({"client_id": app["client_id"], "client_secret": app["client_secret"], "code": code, "redirect_uri": app["redirect_uri"]}))
    a = r.read()
    m = re.search("access_token=(.*)", a)
    token = m.group(1)
    with open("seinbox.token", "w") as f:
        print >>f, token
r = urllib2.urlopen("https://api.stackexchange.com/2.0/inbox/unread?access_token=%s&key=%s" % (token, app["client_key"]))
print zlib.decompress(r.read(), 16+zlib.MAX_WBITS)
