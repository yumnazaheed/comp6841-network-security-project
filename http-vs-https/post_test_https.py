# victim-ubuntu — submits over HTTPS
import urllib.request
import ssl

data = b'username=testuser&password=SuperSecret123'
req = urllib.request.Request('https://192.168.50.30:8443/login', data=data, method='POST')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(urllib.request.urlopen(req, context=ctx).read())
