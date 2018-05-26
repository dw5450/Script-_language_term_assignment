import http.client
import json
import urllib

server = "api.neople.co.kr"
apikey = "9BdgXATgR7uy3XIzIaJPBHfECPoJGKlq"
던파API연결 = http.client.HTTPSConnection(server)

게임서버사전 = {'카인' : 'cain', '디레지에' : 'diregie', "시로코" :'siroco',
                  '프레이' : 'prey', '카시야스' : 'casillas', '힐더' : 'hilder',
                  '안톤' : 'anton', '바칼' : 'bakal'}


def 캐릭터정보불러오기(서버이름, 캐릭터이름):
    # myApiKey = "9BdgXATgR7uy3XIzIaJPBHfECPoJGKlq"

    서버아이디 = 게임서버사전[서버이름]
    캐릭터이름= urllib.parse.quote(캐릭터이름)
    던파API연결.request("GET", "https://api.neople.co.kr/df/servers/"+서버아이디+"/characters?characterName=" +캐릭터이름 + "&limit=<limit>&wordType=<wordType>&apikey=" + apikey) #서버에 GET 요청
    req = 던파API연결.getresponse() 			#openAPI 서버에서 보내온 요청을 받아옴
    #print(req.status, req.reason)
    if(req.status == 200):
        cLen = req.getheader("Content-Length") 	#가져온 데이터 길이
        data = req.read(int(cLen))
        dict = json.loads(data)

        캐릭터아이디 = dict['rows'][0]["characterId"]

        던파API연결.request("GET", "https://api.neople.co.kr/df/servers/" +서버아이디+ "/characters/"+캐릭터아이디+"/equip/equipment?apikey=" + apikey) #서버에 GET 요청
        req = 던파API연결.getresponse() 			#openAPI 서버에서 보내온 요청을 받아옴
        cLen = req.getheader("Content-Length") 	#가져온 데이터 길이
        data = req.read(int(cLen))
        dict = json.loads(data)

        return dict

    else : return False



def 장비설명불러오기(장비아이디):
    던파API연결.request("GET",
                    "https://api.neople.co.kr/df/items/" + 장비아이디 + "?apikey=" + apikey)  # 서버에 GET 요청
    req = 던파API연결.getresponse()
    cLen = req.getheader("Content-Length")  # 가져온 데이터 길이
    data = req.read(int(cLen))
    dict = json.loads(data)
    return dict['itemExplain']
