# victim-ubuntu — submits plaintext HTTP login
import urllib.request
data = b'username=testuser&password=SuperSecret123'
req = urllib.request.Request('http://192.168.50.30:8080/login', data=data, method='POST')
print(urllib.request.urlopen(req).read())
