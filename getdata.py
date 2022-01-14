import requests

base_url = 'http://127.0.0.1:5000/'

req = requests.put(base_url +'/data/5',{"name":"Rendy orton",'ether':"0xfc",'ammount':1})
print(req.json())
