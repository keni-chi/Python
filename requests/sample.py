import requests

headers = {'x-amzn-iot-thingname': '{モノ名}'}
url = 'https://{アカウントとリージョン固有文字列}.credentials.iot.ap-northeast-1.amazonaws.com/role-aliases/{ロールエイリアス}/credentials'
certs = ('xxx.pem.certのファイルパス', 'private.pem.keyのファイルパス')
r = requests.get(url, cert =certs, headers=headers)
print(r)
print(r.content)
print(r.text)
print(r.json)
