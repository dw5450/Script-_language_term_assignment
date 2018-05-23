import http.client
import json
import urllib


server = "api.neople.co.kr"
conn = http.client.HTTPSConnection(server)


serverId = 'cain'
CharaterName = urllib.parse.quote("비구름마녀")

conn.request("GET", "https://api.neople.co.kr/df/servers/cain/characters?characterName=" +CharaterName + "&limit=<limit>&wordType=<wordType>&apikey=9BdgXATgR7uy3XIzIaJPBHfECPoJGKlq") #서버에 GET 요청
req = conn.getresponse() 			#openAPI 서버에서 보내온 요청을 받아옴
print(req.status, req.reason)
cLen = req.getheader("Content-Length") 	#가져온 데이터 길이
data = req.read(int(cLen))
dict = json.loads(data)

charaterId = dict['rows'][0]["characterId"]


conn.request("GET", "https://api.neople.co.kr/df/servers/" +serverId+ "/characters/"+charaterId+"/equip/equipment?apikey=9BdgXATgR7uy3XIzIaJPBHfECPoJGKlq") #서버에 GET 요청
#https://api.neople.co.kr/df/servers/<serverId>/characters/<characterId>/equip/equipment?apikey=9BdgXATgR7uy3XIzIaJPBHfECPoJGKlq
req = conn.getresponse() 			#openAPI 서버에서 보내온 요청을 받아옴
print(req.status, req.reason)
cLen = req.getheader("Content-Length") 	#가져온 데이터 길이
data = req.read(int(cLen))
dict = json.loads(data)

print (dict)