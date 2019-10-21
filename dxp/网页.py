import requests
res = requests.get('http://www.ucas.ac.cn')
res.encoding = 'utf-8'
print(res.text)
