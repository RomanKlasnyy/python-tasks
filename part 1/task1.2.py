"""2) Write regular expression to retrieve domain name(s) from given string
(urls with schema and www should be processed)."""

import re

phrase = '''
I told him to visit https://regexr.com/, 
but he decided to check www.fakeregexr.com/ 
or even http://veryfakeregexr.com/ OMG, it is so unsecure UwU
'''

result = re.findall(r'(w{3}.\w+\.\w+)', phrase)          # triggers on www. only
result_http = re.findall(r'(\w+:\/\/\w+\.\w+)', phrase)  # for http and https.
result.extend(result_http)

print(result)
