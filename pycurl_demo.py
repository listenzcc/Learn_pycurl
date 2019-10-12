# coding: utf-8

import pycurl
import certifi
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://cn.bing.com/th?id=OIP.br1E-X-QilPetY__yvCOZgHaFr&pid=Api&rs=1')
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(len(body))
# print(body)

with open('a.jpeg', 'wb') as f:
    f.write(body)
