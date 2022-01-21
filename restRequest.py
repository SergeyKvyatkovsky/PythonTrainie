import requests

API_KEY = 'pdct.1.1.20220114T084336Z.535ecff4ab98c286.ffb64bf19bb17e025ae70e0b48a5f4faa8eba44a'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
params = dict(key=API_KEY, text='Hello', lang='en-es')

res = requests.get('https://scotch.io');
translater = requests.get(url,params=params,timeout=200);



print(translater.json)
#print(ss.headers)
#print(ss.content)
#print(ss.text)




