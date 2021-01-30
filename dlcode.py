import requests
import re

allurl =__import__('config').getallurl()

for url in allurl:
  print(url)
  content = requests.get(url).text
  scriptname = re.findall(r'\w+\.py', url, re.S)[0]
  with open('./'+scriptname, 'w', encoding='utf-8') as f:
    f.write(content.replace('\r\n', '\n'))
    print('raw下载写入成功：'+scriptname)
    f.close()