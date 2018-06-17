import telepot
from urllib.request import urlopen
import time
import noti
from 캐릭터정보 import *


서버Callcnt = 0
handleCallCnt = 0
서버 = None
이름 = None
타입 = None
캐릭터 = None

고인물전투력 = {'독립공격력': 762652.38, "물리공격력": 7623841.0, "마법공격력": 7623841.0}
노오력전투력 = {'독립공격력': 146841.49, "물리공격력": 1466123.27, "마법공격력": 1466123.27}
퀘전전투력 = {'독립공격력': 20583.06, "물리공격력": 206496.24, "마법공격력": 206496.24}

게임서버사전 = {'카인' : 'cain', '디레지에' : 'diregie', "시로코" :'siroco',
                  '프레이' : 'prey', '카시야스' : 'casillas', '힐더' : 'hilder',
                  '안톤' : 'anton', '바칼' : 'bakal'}


def handle(msg):
    global 서버
    global 이름
    global 타입
    global 캐릭터
    global 게임서버사전
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return
    global handleCallCnt

    text = msg['text']
    args = text.split(' ')


    if text.startswith('시작') or text.startswith('정보'):
        noti.sendMessage(chat_id, '던파 전투력을 측정해드립니다. 서버 캐릭터서버 입력 후 순서대로 따라가주세요!')
        noti.sendMessage(chat_id, '예) 서버 카인  -> 이름 비구름마녀  -> 타입 독립공격력  -> 측정')
        noti.sendMessage(chat_id, "서버 서버명 을 입력해 주세요.")

    elif text.startswith('서버'):
        print('try to 지역', args[1])
        서버 = args[1]
        if 서버 in 게임서버사전.keys():
            noti.sendMessage(chat_id, '이름 이름명 을 입력해주세요')
        else:
            noti.sendMessage(chat_id, '해당 서버는 존재하지 않아요')

    elif text.startswith('이름')  and len(args)>1:
        print('try to 이름', args[1])
        이름  = args[1]
        noti.sendMessage(chat_id, '타입 타입명(물리공격력/마법공격력/독립공격력) 을 입력해주세요')

    elif text.startswith('타입') and len(args)>1:
        print('try to 타입')
        타입 = args[1]
        noti.sendMessage(chat_id, '측정 을 입력해주세요.')

    elif text.startswith('측정'):
        if(서버 in 게임서버사전.keys() and 이름 != None):
            캐릭터 =  캐릭터정보()
            캐릭터.캐릭터불러오기(서버, 이름)
        else:
            noti.sendMessage(chat_id, '서버나 이름이 설정되지 않았어요.')

        if (캐릭터 !=None and 타입 in 퀘전전투력.keys()):
            캐릭터전투력 = 캐릭터.전투력계산(타입)
            noti.sendMessage(chat_id, '서버 : ' + 서버 )
            noti.sendMessage(chat_id, '이름 : ' + 이름)
            noti.sendMessage(chat_id, str(캐릭터전투력/퀘전전투력[타입])  + ' 퀘전')
            noti.sendMessage(chat_id, str(캐릭터전투력/노오력전투력[타입]) +  ' 노오력')
            noti.sendMessage(chat_id, str(캐릭터전투력/고인물전투력[타입]) + ' 고인물')

        else:
            noti.sendMessage(chat_id, '케릭터가 설정되지 못하였거나 타입이 잘못 설정되었어요')

    else:
        noti.sendMessage(chat_id, '모르는 명령어입니다.\n 명령어에 대하여 궁금하시다면 정보 를 입력해주세요.')




bot = telepot.Bot(noti.TOKEN)
print( bot.getMe() )
bot.message_loop(handle)
print('Listening...')
while 1:
    time.sleep(10)
    print(서버, 이름, 타입)


