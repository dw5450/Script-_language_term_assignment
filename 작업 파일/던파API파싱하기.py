import http.client
import json
import urllib

server = "api.neople.co.kr"
apikey = "9BdgXATgR7uy3XIzIaJPBHfECPoJGKlq"
던파API연결 = http.client.HTTPSConnection(server)

게임서버사전 = {'카인' : 'cain', '디레지에' : 'diregie', "시로코" :'siroco',
                  '프레이' : 'prey', '카시야스' : 'casillas', '힐더' : 'hilder',
                  '안톤' : 'anton', '바칼' : 'bakal'}


def 캐릭터연결확인하기(서버이름, 캐릭터이름):
    서버아이디 = 게임서버사전[서버이름]
    캐릭터이름 = urllib.parse.quote(캐릭터이름)
    던파API연결.request("GET", "https://api.neople.co.kr/df/servers/" + 서버아이디 + "/characters?characterName=" + 캐릭터이름 + "&limit=<limit>&wordType=<wordType>&apikey=" + apikey)  # 서버에 GET 요청
    req = 던파API연결.getresponse()  # openAPI 서버에서 보내온 요청을 받아옴
    # print(req.status, req.reason)
    if (req.status == 200):
        return True

    else : return False

def 캐릭터장비사전불러오기(서버이름, 캐릭터이름):
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

        던파API연결.request("GET",
                        "https://api.neople.co.kr/df/servers/" + 서버아이디 + "/characters/" + 캐릭터아이디 + "/equip/creature?apikey=" + apikey)  # 서버에 GET 요청
        req = 던파API연결.getresponse()  # openAPI 서버에서 보내온 요청을 받아옴
        cLen = req.getheader("Content-Length")  # 가져온 데이터 길이
        data = req.read(int(cLen))
        크리처정보사전 = json.loads(data)

        dict['equipment'].append(크리처정보사전['creature'])
        req.close()
        던파API연결.close()
        return dict['equipment']


    else :
        req.close()
        던파API연결.close()
        return False


def 캐릭터스탯사전불러오기(서버이름, 캐릭터이름):
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

        던파API연결.request("GET", "https://api.neople.co.kr/df/servers/" +서버아이디+ "/characters/"+캐릭터아이디+"/status?apikey=" + apikey) #서버에 GET 요청
        req = 던파API연결.getresponse() 			#openAPI 서버에서 보내온 요청을 받아옴
        cLen = req.getheader("Content-Length") 	#가져온 데이터 길이
        data = req.read(int(cLen))
        dict = json.loads(data)
        req.close()
        던파API연결.close()
        return dict

    else :
        req.close()
        던파API연결.close()
        return False


def 장비가져오기(아이템이름):
    아이템이름 = urllib.parse.quote(아이템이름)
    던파API연결.request("GET", "https://api.neople.co.kr/df/items?itemName=" + 아이템이름 + "&q=minLevel:<minLevel>,maxLevel:<maxLevel>,rarity:<rarity>,trade:<trade>&limit=<limit>&wordType=<wordType>&apikey=" + apikey)  # 서버에 GET 요청
    req = 던파API연결.getresponse()
    cLen = req.getheader("Content-Length")  # 가져온 데이터 길이
    data = req.read(int(cLen))
    dict = json.loads(data)
    req.close()
    던파API연결.close()
    return dict['rows'][0]

def 장비설명불러오기(장비아이디):
    던파API연결.request("GET", "https://api.neople.co.kr/df/items/" + 장비아이디 + "?apikey=" + apikey)  # 서버에 GET 요청
    req = 던파API연결.getresponse()
    cLen = req.getheader("Content-Length")  # 가져온 데이터 길이
    data = req.read(int(cLen))
    dict = json.loads(data)
    req.close()
    던파API연결.close()
    return dict['itemExplain']

