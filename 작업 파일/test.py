import telepot
from urllib.request import urlopen
import time
import noti


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')
    if text.startswith('서버') and len(args)>1:
        print('try to 지역', args[1])
        #replyAptData( '201801', chat_id, args[1] )
    elif text.startswith('이름')  and len(args)>1:
        print('try to 저장', args[1])
        #save( chat_id, args[1] )
    elif text.startswith('타입'):
        print('try to 확인')
        #check( chat_id )
    else:
        noti.sendMessage(chat_id, '모르는 명령어입니다.\n서버 [서버], 이름 [캐릭터이름], 타입 [공격타입(물리공격력/마법공격력/독립공격력) 확인 중 하나의 명령을 입력하세요.')




bot = telepot.Bot(noti.TOKEN)
print( bot.getMe() )
bot.message_loop(handle)
print('Listening...')
while 1:
    time.sleep(10)


