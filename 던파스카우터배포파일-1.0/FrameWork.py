import urllib
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk

from 던파API파싱하기 import *
from 캐릭터정보 import *
from myTk import *
from 메일보내기용 import *
from tkinter import *
import copy


고인물전투력 = {'독립공격력': 762652.38, "물리공격력": 7623841.0, "마법공격력": 7623841.0}
노오력전투력 = {'독립공격력': 146841.49, "물리공격력": 1466123.27, "마법공격력": 1466123.27}
퀘전전투력 = {'독립공격력': 20583.06, "물리공격력": 206496.24, "마법공격력": 206496.24}

기준캐릭터 = None
측정캐릭터 = None
임시캐릭터 = None

class 던파스카우터프레임워크:
    #생성자
    def __init__(self):
        self.Tk_Position = {'x' : 600, 'y' : 150} #Tk의 위치
        self.Scene = None
        self.메뉴Tk()  # 신에 메뉴Tk를 설정한다.

        self.status = None



    #메뉴 Tk
    def 메뉴Tk(self):

        self.status = '메뉴'

        if (self.Scene != None):
            self.Scene.destroy()

        메뉴_Tk = Tk()
        메뉴_Tk.geometry(Tk크기설명(250, 320, self.Tk_Position['x'], self.Tk_Position['y']))

        photo = PhotoImage(file="던파_로고.png")
        # 디폴트 이미지 파일
        imageLabel = Label(메뉴_Tk, image=photo)
        imageLabel.place(x = -20, y = 70)

        Tk글쓰기(메뉴_Tk, 20, 'bold', '[던파스카우터]', 25, 10)
        Tk버튼만들기(메뉴_Tk, 15, 'bold', '캐릭터불러오기', self.캐릭터불러오기, 45, 60)
        Tk버튼만들기(메뉴_Tk, 15, 'bold', '캐릭터설정하기', self.캐릭터설정하기Tk, 45, 105)
        Tk버튼만들기(메뉴_Tk, 15, 'bold', '전투력측정하기', self.전투력측정하기, 45, 150)
        Tk버튼만들기(메뉴_Tk, 15, 'bold', '     메일    ', self.메일, 45, 195)
        Tk버튼만들기(메뉴_Tk, 15, 'bold', '     종료    ', self.종료, 45, 240)

        self.Scene = 메뉴_Tk

        메뉴_Tk.mainloop()



    #캐릭터 불러오기
    def 측정(self):
        global 캐릭터저장타입
        캐릭터저장타입 = '측정'

    def 기준(self):
        global 캐릭터저장타입
        캐릭터저장타입 = '기준'

    def 임시캐릭터불러오기(self):
        global 캐릭터불러오기_Tk
        global 서버리스트박스
        global 캐릭터이름입력창
        global 임시캐릭터

        서버 = 서버리스트박스.get(int(서버리스트박스.yview()[0] * 8))
        이름 = 캐릭터이름입력창.get()

        임시캐릭터 = 캐릭터정보()
        임시캐릭터.캐릭터불러오기(서버, 이름)
        #임시캐릭터.이미지 = 캐릭터이미지가져오기(서버, 이름)

        string = "이름 : " + 임시캐릭터.이름 + '\n'
        string += '직업 : ' + 임시캐릭터.직업 + '\n'
        Tk출력창만들기(캐릭터불러오기_Tk, 10, 25, 10, string, 215, 70)

    def 임시캐릭터저장하기(self):
        global 캐릭터불러오기_Tk
        global 캐릭터저장타입
        global 측정캐릭터
        global 임시캐릭터
        global 기준캐릭터

        if 캐릭터저장타입 == '측정':
            측정캐릭터 = copy.deepcopy(임시캐릭터)
        elif 캐릭터저장타입 == '기준':
            기준캐릭터 = copy.deepcopy(임시캐릭터)

        Tk출력창만들기(캐릭터불러오기_Tk, 10, 25, 10, '저장되었습니다.', 215, 70)

    def 캐릭터불러오기(self):
        self.status = '캐릭터불러오기'
        global 서버리스트박스
        global 캐릭터이름입력창
        global 임시캐릭터
        global 기준캐릭터
        global 측정캐릭터
        global 캐릭터불러오기_Tk
        #Tk생성
        캐릭터불러오기_Tk = Tk()
        캐릭터불러오기_Tk.geometry(Tk크기설명(400, 210, self.Tk_Position['x'] - 100, self.Tk_Position['y']))

        #제목쓰기
        Tk글쓰기(캐릭터불러오기_Tk, 20, 'bold', '[던파스카우터]', 100, 10)

        #서버 선택창 만들기
        Tk글쓰기(캐릭터불러오기_Tk, 15, 'bold', '서버', 0, 60)
        서버리스트 = ['카인', '디레지에', "시로코",
                 '프레이', '카시야스', '힐더',
                 '안톤', '바칼']
        서버리스트박스 = Tk리스트박스만들기(캐릭터불러오기_Tk, 15, 'bold', 서버리스트, 50, 60)

        #캐릭터이름 입력창 만들기
        Tk글쓰기(캐릭터불러오기_Tk, 15, 'bold', '이름', 0, 90)
        캐릭터이름입력창 = Tk입력창만들기(캐릭터불러오기_Tk, 12, 'bold', 15, 50, 90)

        #저장타입 선택 라디오버튼만들기
        Tk라디오버튼만들기(캐릭터불러오기_Tk, '측정', 1, self.측정, 120, 180)
        Tk라디오버튼만들기(캐릭터불러오기_Tk, '기준', 0, self.기준, 120, 160)

        #명령 버튼 만들기
        Tk버튼만들기(캐릭터불러오기_Tk, 12, 'bold', '불러오기', self.임시캐릭터불러오기, 20, 125)
        Tk버튼만들기(캐릭터불러오기_Tk, 12, 'bold', '저장하기', self.임시캐릭터저장하기, 110, 125)
        Tk버튼만들기(캐릭터불러오기_Tk, 12, 'bold', '돌아가기', self.메뉴Tk, 20, 165)

        #불러오기 결과쓰기
        Tk글쓰기(캐릭터불러오기_Tk, 12, 'bold', '불러오기결과', 250, 47)
        Tk출력창만들기(캐릭터불러오기_Tk, 10, 25, 10, '불러온 캐릭터가 없습니다.', 215, 70)

        if self.Scene != None:
            self.Scene.destroy()

        self.Scene = 캐릭터불러오기_Tk

    def 전투력출력하기(self):
        global 전투력측정하기_Tk
        global 공격타입리스트박스
        global 측정타입리스트박스
        global 측정캐릭터
        global 기준캐릭터
        global 퀘전전투력
        global 노오력전투력
        global 고인물전투력

        공격타입 = 공격타입리스트박스.get(int(공격타입리스트박스.yview()[0] * 3))
        측정타입 = 측정타입리스트박스.get(int(측정타입리스트박스.yview()[0] * 4))

        #이미지 추가 필요
        if 측정캐릭터 != None:
            string = '이름 : ' + 측정캐릭터.이름 + '\n\n'
            string += '서버 : ' + 측정캐릭터.서버 + '\n\n'
            string += '직업 : ' + 측정캐릭터.직업 + '\n\n'

            if 측정타입 == '퀘전':
                string += '전투력 : ' + str(int(측정캐릭터.전투력계산(공격타입) / 퀘전전투력[공격타입] * 100) / 100) + ' 퀘전'

            elif 측정타입 == '노력':
                string += '전투력 : ' + str(int(측정캐릭터.전투력계산(공격타입) / 노오력전투력[공격타입] * 100) / 100) + ' 노력'

            elif 측정타입 == '모인물':
                string += '전투력 : ' + str(int(측정캐릭터.전투력계산(공격타입) / 고인물전투력[공격타입] * 100) / 100) + ' 모인물'

            elif 측정타입 == '기준캐릭' and 기준캐릭터 != None:
                string += '전투력 : ' + str(int(측정캐릭터.전투력계산(공격타입) / 기준캐릭터.전투력계산(공격타입) * 100) / 100) + ' ' + 기준캐릭터.이름
            else:
                string = "에러가 발생하였습니다"

            string += '\n\n'

            Tk출력창만들기(전투력측정하기_Tk, 10, 54, 28, string, 30, 110)



    def 전투력측정하기(self):
        self.status = '전투력측정하기'
        global 공격타입리스트박스
        global 측정타입리스트박스
        global 전투력측정하기_Tk
        
        #Tk설정하기
        전투력측정하기_Tk = Tk()
        전투력측정하기_Tk.geometry(Tk크기설명(440, 500, self.Tk_Position['x'] - 150, self.Tk_Position['y']))

        #제목쓰기
        Tk글쓰기(전투력측정하기_Tk, 20, 'bold', '[던파스카우터 : 전투력측정하기]', 0, 0)

        #공격타입 리스트박스
        Tk글쓰기(전투력측정하기_Tk, 12, 'bold', '공격 타입', 25, 40)
        공격타입리스트 = ['물리공격력', '마법공격력', '독립공격력']
        공격타입리스트박스 = Tk리스트박스만들기(전투력측정하기_Tk, 12, 'bold', 공격타입리스트, 110, 40)

        #측정타입 리스트박스
        Tk글쓰기(전투력측정하기_Tk, 12, 'bold', '측정 타입', 25, 70)
        측정타입리스트 = ['퀘전', '노력', '모인물', '기준캐릭']
        측정타입리스트박스 = Tk리스트박스만들기(전투력측정하기_Tk, 12, 'bold', 측정타입리스트, 110, 70)

        #버튼만들기
        Tk버튼만들기(전투력측정하기_Tk, 12, 'bold', '측정하기', self.전투력출력하기, 260, 40)
        Tk버튼만들기(전투력측정하기_Tk, 12, 'bold', '돌아가기', self.메뉴Tk, 340, 40)

        Tk출력창만들기(전투력측정하기_Tk, 10, 54, 28, '', 30, 110)

        if self.Scene != None:
            self.Scene.destroy()

        self.Scene = 전투력측정하기_Tk


    def 아이템불러오기(self):
        global 아이템이름입력창
        global 캐릭터설정하기_Tk
        global 불러온장비
        아이템이름  =  str(아이템이름입력창.get())
        불러온장비 = 장비가져오기(아이템이름)

        #추후 이미지 추가?

        string  = "이름 : " + 불러온장비['itemName'] + '\n\n'
        string += "등급 : " + 불러온장비['itemRarity'] + '\n\n'
        string += "타입 : " + 불러온장비['itemType'] + '\n\n'
        string += "레밸 : " + str(불러온장비['itemAvailableLevel']) + '\n\n'
        Tk출력창만들기(캐릭터설정하기_Tk, 10, 24, 13, string, 20, 210)

    def 아이템저장캐릭측정(self):
        global 아이템저장캐릭터타입
        global 캐릭터설정하기_Tk
        global 측정캐릭터
        아이템저장캐릭터타입 = '측정'

        string = self.캐릭터사전string('출력', 측정캐릭터)

        Tk출력창만들기(캐릭터설정하기_Tk, 10, 38, 23, string, 210, 75)

    def 아이템저장캐릭기준(self):
        global 아이템저장캐릭터타입
        global 기준캐릭터
        아이템저장캐릭터타입 = '기준'

        string = self.캐릭터사전string('기준', 기준캐릭터)

        Tk출력창만들기(캐릭터설정하기_Tk, 10, 38, 23, string, 210, 75)

    def 아이템저장하기(self):
        global 아이템저장캐릭터타입
        global 불러온장비
        global 기준캐릭터
        아이템저장캐릭터타입 = '기준'
        global 측정캐릭터
        아이템저장캐릭터타입 = '측정'

        if 아이템저장캐릭터타입 =='기준':
            기준캐릭터.아이템바꾸기(불러온장비)
        elif 아이템저장캐릭터타입 == '측정':
            측정캐릭터.아이템바꾸기(불러온장비)
        else:
            print('아이템 저장하기에서 오류가 발생하였습니다.')

        string = self.캐릭터사전string(아이템저장캐릭터타입, 기준캐릭터)

        Tk출력창만들기(캐릭터설정하기_Tk, 10, 38, 23, string, 210, 75)



    def 캐릭터사전string(self, 아이템저장캐릭터타입, 출력캐릭터):
        if 아이템저장캐릭터타입 == '기준':
            출력캐릭터  = 기준캐릭터
        if 아이템저장캐릭터타입 == '측정':
            출력캐릭터  = 측정캐릭터

        if 출력캐릭터 != None:
            string = "무기 : " + 출력캐릭터.캐릭터장비사전[0]['itemName'] + '\n\n'
            string += "칭호 : " + 출력캐릭터.캐릭터장비사전[1]['itemName'] + '\n\n'
            string += "상의 : " + 출력캐릭터.캐릭터장비사전[2]['itemName'] + '\n\n'
            string += "머리어깨 : " + 출력캐릭터.캐릭터장비사전[3]['itemName'] + '\n\n'
            string += "하의 : " + 출력캐릭터.캐릭터장비사전[4]['itemName'] + '\n\n'
            string += "신발 : " + 출력캐릭터.캐릭터장비사전[5]['itemName'] + '\n\n'
            string += "허리 : " + 출력캐릭터.캐릭터장비사전[6]['itemName'] + '\n\n'
            string += "목걸이 : " + 출력캐릭터.캐릭터장비사전[7]['itemName'] + '\n\n'
            string += "팔찌 : " + 출력캐릭터.캐릭터장비사전[8]['itemName'] + '\n\n'
            string += "반지 : " + 출력캐릭터.캐릭터장비사전[9]['itemName'] + '\n\n'
            string += "보조장비 : " + 출력캐릭터.캐릭터장비사전[10]['itemName'] + '\n\n'
            string += "마법석 : " + 출력캐릭터.캐릭터장비사전[11]['itemName'] + '\n\n'
            string += "귀걸이 : " + 출력캐릭터.캐릭터장비사전[12]['itemName'] + '\n\n'

        else : string = '캐릭터가 존재하지 않습니다.'

        return string;

    def 캐릭터설정하기Tk(self):

        self.status = '캐릭터설정하기'
        global 캐릭터설정하기_Tk
        global 아이템이름입력창
        global 아이템저장캐릭터타입
        global 불러온장비
        global 기준캐릭터
        global 측정캐릭터

        아이템저장캐릭터타입 = '측정'

        캐릭터설정하기_Tk = Tk()
        캐릭터설정하기_Tk.geometry(Tk크기설명(500, 400, self.Tk_Position['x'] - 100, self.Tk_Position['y']))

        # 제목쓰기
        Tk글쓰기(캐릭터설정하기_Tk, 20, 'bold', '[던파스카우터 : 캐릭터설정하기]', 40, 10)

        # 아이템이름 입력창 만들기
        Tk글쓰기(캐릭터설정하기_Tk, 12, 'bold', '아이템명', 10, 60)
        아이템이름입력창 = Tk입력창만들기(캐릭터설정하기_Tk, 12, 'bold', 12, 80, 60)

        # 명령 버튼 만들기
        Tk버튼만들기(캐릭터설정하기_Tk, 12, 'bold', '불러오기', self.아이템불러오기, 20, 95)
        Tk버튼만들기(캐릭터설정하기_Tk, 12, 'bold', '저장하기', self.아이템저장하기, 110, 95)
        Tk버튼만들기(캐릭터설정하기_Tk, 12, 'bold', '돌아가기', self.메뉴Tk, 20, 135)

        #라디오버튼만들기
        Tk라디오버튼만들기(캐릭터설정하기_Tk, '측정', 1, self.아이템저장캐릭측정, 120, 150)
        Tk라디오버튼만들기(캐릭터설정하기_Tk, '기준', 0, self.아이템저장캐릭기준, 120, 130)

        #출력창 만들기
        Tk글쓰기(캐릭터설정하기_Tk, 12, 'bold', '불러온아이템정보', 40, 180)
        Tk출력창만들기(캐릭터설정하기_Tk, 10, 24, 13, '', 20, 210)
        Tk글쓰기(캐릭터설정하기_Tk, 12, 'bold', '캐릭터장비사전', 285, 50)

        if 아이템저장캐릭터타입 == '기준':
            출력캐릭터  = 기준캐릭터
        if 아이템저장캐릭터타입 == '측정':
            출력캐릭터  = 측정캐릭터

        if 출력캐릭터 != None:
            string = "무기 : " + 출력캐릭터.캐릭터장비사전[0]['itemName'] + '\n\n'
            string += "칭호 : " + 출력캐릭터.캐릭터장비사전[1]['itemName'] + '\n\n'
            string += "상의 : " + 출력캐릭터.캐릭터장비사전[2]['itemName'] + '\n\n'
            string += "머리어깨 : " + 출력캐릭터.캐릭터장비사전[3]['itemName'] + '\n\n'
            string += "하의 : " + 출력캐릭터.캐릭터장비사전[4]['itemName'] + '\n\n'
            string += "신발 : " + 출력캐릭터.캐릭터장비사전[5]['itemName'] + '\n\n'
            string += "허리 : " + 출력캐릭터.캐릭터장비사전[6]['itemName'] + '\n\n'
            string += "목걸이 : " + 출력캐릭터.캐릭터장비사전[7]['itemName'] + '\n\n'
            string += "팔찌 : " + 출력캐릭터.캐릭터장비사전[8]['itemName'] + '\n\n'
            string += "반지 : " + 출력캐릭터.캐릭터장비사전[9]['itemName'] + '\n\n'
            string += "보조장비 : " + 출력캐릭터.캐릭터장비사전[10]['itemName'] + '\n\n'
            string += "마법석 : " + 출력캐릭터.캐릭터장비사전[11]['itemName'] + '\n\n'
            string += "귀걸이 : " + 출력캐릭터.캐릭터장비사전[12]['itemName'] + '\n\n'
        else:
            string = '설정된 캐릭터가 존재하지 않습니다.'

        Tk출력창만들기(캐릭터설정하기_Tk, 10, 38, 23, string, 210, 75)




        if self.Scene != None:
            self.Scene.destroy()

        self.Scene = 캐릭터설정하기_Tk

    def 메일보내기(self):
        global 메일입력창
        global 측정캐릭터
        global 기준캐릭터
        메일주소 = 메일입력창.get()

        if 측정캐릭터 != None:
            info_text = '서버 : ' + 측정캐릭터.서버 + '<br/>'
            info_text +="이름 : " +측정캐릭터.이름 + '<br/>'
            info_text +="직업 : " +측정캐릭터.직업  +'<br/>' + '<br/>'
            info_text +="물리 공력력" +'<br/>'
            info_text +='  퀘전 : ' + str(int(측정캐릭터.전투력계산('물리공격력') / 퀘전전투력['물리공격력'] * 100) / 100) + ' 퀘전' +'<br/>'
            info_text +='  노오력 : ' + str(int(측정캐릭터.전투력계산('물리공격력') / 노오력전투력['물리공격력'] * 100) / 100) + ' 노력'  +'<br/>'
            info_text +='  모인물 : ' + str(int(측정캐릭터.전투력계산('물리공격력') / 고인물전투력['물리공격력'] * 100) / 100) + ' 고인물 ' +'<br/>'
            if 기준캐릭터 != None:
                info_text += '  기준캐릭터 : '+ str(int(측정캐릭터.전투력계산('물리공격력') / 기준캐릭터.전투력계산('물리공격력') * 100) / 100) + ' ' + 기준캐릭터.이름  +'<br/>'
            info_text  +='<br/>'

            info_text += "마법 공력력"  +'<br/>'
            info_text += '  퀘전 : ' + str(int(측정캐릭터.전투력계산('마법공격력') / 퀘전전투력['마법공격력'] * 100) / 100)  +'<br/>'
            info_text += '  노오력 : ' + str(int(측정캐릭터.전투력계산('마법공격력') / 노오력전투력['마법공격력'] * 100) / 100)  +'<br/>'
            info_text += '  모인물 : ' + str(int(측정캐릭터.전투력계산('마법공격력') / 고인물전투력['마법공격력'] * 100) / 100)  +'<br/>'
            if 기준캐릭터 != None:
                info_text += '  기준캐릭터 : ' + str(int(측정캐릭터.전투력계산('마법공격력') / 기준캐릭터.전투력계산('마법공격력') * 100) / 100) + ' ' + 기준캐릭터.이름  +'<br/>'
            info_text  += '<br/>'

            info_text += "독립 공력력"  +'<br/>'
            info_text += '  퀘전 : ' + str(int(측정캐릭터.전투력계산('독립공격력') / 퀘전전투력['독립공격력'] * 100) / 100) + ' 퀘전' +'<br/>'
            info_text += '  노오력 : ' + str(int(측정캐릭터.전투력계산('독립공격력') / 노오력전투력['독립공격력'] * 100) / 100) + ' 노력'  +'<br/>'
            info_text += '  모인물 : ' + str(int(측정캐릭터.전투력계산('독립공격력') / 고인물전투력['독립공격력'] * 100) / 100) + ' 고인물'  +'<br/>'
            if 기준캐릭터 != None:
                info_text += '  기준캐릭터 : ' + str(int(측정캐릭터.전투력계산('독립공격력') / 기준캐릭터.전투력계산('독립공격력') * 100) / 100) + ' ' + 기준캐릭터.이름  +'<br/>'
            info_text  +='<br/>'


        else :
            info_text = "설정을 하지 않으셨어요."  +'<br/>'

        SendMail(메일주소, info_text)

    def 메일(self):
        self.status = '메일'
        global 메일입력창
        메일_Tk = Tk()
        메일_Tk.geometry(Tk크기설명(300, 150, self.Tk_Position['x'] - 100, self.Tk_Position['y']))

        Tk글쓰기(메일_Tk, 20, 'bold', '[던파스카우터 : 메일]', 0, 10)

        # 아이템이름 입력창 만들기
        Tk글쓰기(메일_Tk, 12, 'bold', '메일 주소', 10, 60)
        메일입력창 = Tk입력창만들기(메일_Tk, 12, 'bold', 20, 90, 60)

        # 명령 버튼 만들기
        Tk버튼만들기(메일_Tk, 12, 'bold', '메일보내기', self.메일보내기, 40, 95)
        Tk버튼만들기(메일_Tk, 12, 'bold', '돌아가기', self.메뉴Tk, 180, 95)

        if self.Scene != None:
            self.Scene.destroy()

        self.Scene = 메일_Tk

    def 종료(self):
        self.Scene.destroy()

    def 실행하기(self):
        self.Scene.mainloop()


fw = 던파스카우터프레임워크()
fw.실행하기()
