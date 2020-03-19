import json
import requests
from bs4 import BeautifulSoup
 
url = 'https://www.zeropay.or.kr/intro/frncSrchList_json.do?'

params = 'pageIndex=1' + '&recordCountPerPage=10' + '&tryCode=01' + '&skkCode=09'
params2 = ''
data = ''

for i in range(0, 5590, 10):
  params2 = '&firstIndex=' + str(i + 1) + '&lastIndex=' + str(i + 10)
  res = requests.get(url + params + params2)
  soup = BeautifulSoup(res.content, 'html.parser')
  site_json=json.loads(soup.text)
  for r in site_json['list']:
    data += "'" + r['pobsAfstrName'] + "','" + r['pobsBaseAddr'] + "','" + r['bztypName'] + "'\r\n"

f = open('zeropay_output.csv', 'w')
f.write(data)
f.close()