import urllib.request

req = urllib.request.Request('http://www.baidu.com')
with urllib.request.urlopen(req) as response:
   the_page = response.read()


print('Status:', response.status,response.reason)
for k, v in response.getheaders():
    print('%s: %s' % (k, v))
print('Data:', the_page.decode('utf-8'))

#from urllib import request

#with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#    data = f.read()
#    print('Status:', f.status, f.reason)
#    for k, v in f.getheaders():
#        print('%s: %s' % (k, v))
#    print('Data:', data.decode('utf-8'))
