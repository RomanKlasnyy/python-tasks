"""3) Write regular expression for parsing links and links titles from simple html."""

import re

html = '''<div class="links">
      <div class="link">
        <a class="first-link" href="google.com">
          <span class="title">Google</span>
          <span class="desc">Google Inc.</span>
        </a>      
      </div>
      <div class="link">
        <a href="www.apple.com" class="second-link" >
          <span class="title">Apple</span>
          <span class="desc">Apple Inc.</span>
        </a>              
      </div>
      <div class="link">
        <a href="https://www.w3schools.com/"  target="_blank"  >
          <span class="title">W3Schools</span>
          <span class="desc">W3Schools Org.</span>
        </a>        
      </div>
    </div>'''

href_list = re.findall(r'href=[\'"]?([^\'" >]+)', html)
title_list = re.findall(r'title">[\'"]?(\w+)', html)
desc_list = re.findall(r'desc">[\'"]?(\w+.*)<', html)

result = []
for i in range(len(href_list)):
    tuple_result = (href_list[i], title_list[i], desc_list[i])
    result.append(tuple_result)

print(result)
