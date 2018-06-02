from 던파API파싱하기 import *
import spam
from 세트아이템사전 import *

class 캐릭터정보 :
    def __init__(self):
        self.__캐릭터스탯사전 = None
        self.__캐릭터장비사전 = None
        self.__나의세트아이템사전 = {}

        self.이름 = ""
        self.__캐릭터타입 = None
        self.직업 = None
        self.__힘 = 0
        self.__지능 = 0
        self.__물리공격력 = 0
        self.__마법공격력 = 0
        self.__독립공격력 = 0
        self.__크리티컬 = 0 # 높은 크리티컬만 저장
        self.__속성강화 = 0#가장 강한 속성만들을 저장

        self.__힘_지능_증가 = 0
        self.__물리_마법_독립_공격력증가 = 0
        self.__증가데미지 = 0
        self.__추가증가데미지 = 0
        self.__크리티컬증가데미지 = 0
        self.__추가크리티컬증가데미지 =0
        self.__추가데미지 = 0
        self.__속성추가데미지 = 0
        self.__모든공격력증가 = 0
        self.__스킬공격력증가 = 0
        self.__방어력감소 = 0
        self.__전투력 = 0

    def __증가량해석(self, 증가량):
        l = list(증가량)
        result = 0
        for data in l:
            if '0' <= data <= '9':
                result = result * 10 + int(data)

            else : break

        return result

    def 전투력가져오기(self):
        return self.__전투력


    def 전투력계산(self, 공격력적용방식):
        힘or지능 = 0
        공격력  = 0
        if 공격력적용방식 == '독립공격력':
            if (self.__힘 < self.__지능):
                힘or지능 = self.__지능
            else: 힘or지능 = self.__힘

            공격력 = self.__독립공격력

        elif 공격력적용방식 == '물리공격력':
            힘or지능 = self.__힘
            공격력 = self.__물리공격력

        elif 공격력적용방식 == '마법공격력':
            힘or지능 = self.__지능
            공격력 = self.__마법공격력


        self.__전투력 = spam.CalPower(
            힘or지능,
            공격력,
            self.__크리티컬,
            self.__속성강화,
            self.__힘_지능_증가,
            self.__물리_마법_독립_공격력증가,
            self.__증가데미지,
            self.__추가증가데미지,
            self.__크리티컬증가데미지,
            self.__추가크리티컬증가데미지,
            self.__추가데미지,
            self.__속성추가데미지,
            self.__모든공격력증가,
            self.__스킬공격력증가,
            self.__방어력감소
        )

    def __초기화(self):
        self.__캐릭터스탯사전 = None
        self.__캐릭터장비사전 = None
        self.__나의세트아이템사전 = {}

        self.이름 = ""
        self.__캐릭터타입 = None
        self.직업 = None
        self.__힘 = 0
        self.__지능 = 0
        self.__물리공격력 = 0
        self.__마법공격력 = 0
        self.__독립공격력 = 0
        self.__크리티컬 = 0  # 높은 크리티컬만 저장
        self.__속성강화 = 0  # 가장 강한 속성만들을 저장

        self.__힘_지능_증가 = 0
        self.__물리_마법_독립_공격력증가 = 0
        self.__증가데미지 = 0
        self.__추가증가데미지 = 0
        self.__크리티컬증가데미지 = 0
        self.__추가크리티컬증가데미지 = 0
        self.__추가데미지 = 0
        self.__속성추가데미지 = 0
        self.__모든공격력증가 = 0
        self.__스킬공격력증가 = 0
        self.__방어력감소 = 0
        self.__전투력 = 0
        
    def __장비설명해석후적용(self, 장비설명):
        설명단어리스트 = 장비설명.split()

        #print(설명단어리스트)
        for i in range(len(설명단어리스트)):
            if 설명단어리스트[i] == '공격':
                if 설명단어리스트[i+3] == '증가량':
                    if 설명단어리스트[i-1] == '크리티컬':
                        self.__추가크리티컬증가데미지 += self.__증가량해석(설명단어리스트[i+4])
                    else :
                        self.__추가증가데미지 += self.__증가량해석(설명단어리스트[i+4])

                elif 설명단어리스트[i+3] == '추가' or 설명단어리스트[i+3] == '추가데미지':
                    self.__추가데미지 += self.__증가량해석(설명단어리스트[i+2])

                elif 설명단어리스트[i + 3] == '속성':
                    self.__속성추가데미지 += self.__증가량해석(설명단어리스트[i + 2])

                elif 설명단어리스트[i-1] == '크리티컬':
                    장비크리티컬증가데미지 = self.__증가량해석(설명단어리스트[i + 3])
                    if self.__크리티컬증가데미지 <  장비크리티컬증가데미지:
                        self.__크리티컬증가데미지 = 장비크리티컬증가데미지
                else :
                    장비증가데미지 = self.__증가량해석(설명단어리스트[i + 3])
                    if self.__증가데미지 < 장비증가데미지:
                        self.__증가데미지 = 장비증가데미지


            elif 설명단어리스트[i] == '공격력':
                if 설명단어리스트[i-1] == '모든':
                    self.__모든공격력증가  = self.__모든공격력증가 + self.__증가량해석(설명단어리스트[i+1])

                elif 설명단어리스트[i-1] == '스킬':
                    self.__스킬공격력증가  = (1+ self.__스킬공격력증가/100) * (1 + self.__증가량해석(설명단어리스트[i+1])/100) * 100 -100

                elif 설명단어리스트[i-1] == '독립':
                    self.__물리_마법_독립_공격력증가 = self.__물리_마법_독립_공격력증가  + self.__증가량해석(설명단어리스트[i+1])

            elif 설명단어리스트[i] == '지능':
                self.__힘_지능_증가 = self.__힘_지능_증가  + self.__증가량해석(설명단어리스트[i + 1])

            elif 설명단어리스트[i]  =='방어력':
                self.__방어력감소 = self.__증가량해석(설명단어리스트[i+1])


    def 캐릭터장비사전저장하기(self, 캐릭터장비사전):
        self.__캐릭터장비사전 = 캐릭터장비사전

    def 캐릭터장비사전적용하기(self):
        for 장비정보 in self.__캐릭터장비사전:
            장비아이디 = 장비정보['itemId']
            if 'setItemName' in 장비정보.keys():
                if 장비정보['setItemName'] in self.__나의세트아이템사전.keys():
                    self.__나의세트아이템사전[장비정보['setItemName']]['num'] += 1

                else : self.__나의세트아이템사전[장비정보['setItemName']] =  {'level': 장비정보['itemAvailableLevel'], 'type' : 장비정보['itemType'], 'num' : 1}
            장비설명=장비설명불러오기(장비아이디)
            self.__장비설명해석후적용(장비설명)

        for key  in self.__나의세트아이템사전.keys():
            if  self.__나의세트아이템사전[key]['type'] == '방어구':
                if self.__나의세트아이템사전[key]['num'] > 4:
                    if key in 세트아이템_5.keys():
                        self.__장비설명해석후적용(세트아이템_5[key])

                if self.__나의세트아이템사전[key]['level'] == 90 and self.__나의세트아이템사전[key]['num'] > 2:
                    if key in 세트아이템_3.keys():
                        self.__장비설명해석후적용(세트아이템_3[key])
            else:
                if key == '바이라바의 계승자' and self.__나의세트아이템사전[key]['num'] > 1:
                    if key in 세트아이템_2.keys():
                        self.__장비설명해석후적용(세트아이템_2[key])

                if self.__나의세트아이템사전[key]['num'] > 2:
                    if key in 세트아이템_3.keys():
                        self.__장비설명해석후적용(세트아이템_3[key])

        ##추후에 장비 아이템 적용 알고리즘 변경

    def 캐릭터스탯사전저장하기(self, 캐릭터스탯사전):
        self.__캐릭터스탯사전 =  캐릭터스탯사전

    def 캐릭터스탯사전적용하기(self):
        self.이름 = self.__캐릭터스탯사전['characterName']
        self.직업 = self.__캐릭터스탯사전['jobGrowName']
        self.__힘 = self.__캐릭터스탯사전['status'][2]['value']
        self.__지능 = self.__캐릭터스탯사전['status'][3]['value']
        self.__물리공격력 = self.__캐릭터스탯사전['status'][6]['value']
        self.__마법공격력 = self.__캐릭터스탯사전['status'][7]['value']
        self.__독립공격력 = self.__캐릭터스탯사전['status'][8]['value']

        if(self.__캐릭터스탯사전['status'][11]['value'] < self.__캐릭터스탯사전['status'][12]['value']):
            self.__크리티컬 = self.__캐릭터스탯사전['status'][12]['value']
        else:
            self.__크리티컬 = self.__캐릭터스탯사전['status'][11]['value']

        self.__속성강화 = 0  # 가장 강한 속성만들을 저장

        for i in range(0, 6, 2):
            if(self.__속성강화 < self.__캐릭터스탯사전['status'][23 + i]['value']):
                self.__속성강화 = self.__캐릭터스탯사전['status'][23 + i]['value']

    def 캐릭터가져오기(self, 서버, 이름):
        self.__초기화()
        self.캐릭터장비사전저장하기(캐릭터장비사전불러오기(서버, 이름))
        self.캐릭터장비사전적용하기()
        self.캐릭터스탯사전저장하기(캐릭터스탯사전불러오기(서버, 이름))
        self.캐릭터스탯사전적용하기()


    def 출력(self):
        print("이름 : ", self.이름)
        print("직업 : ", self.직업)
        print("힘 : ", self.__힘)
        print("지능 :", self.__지능)
        print("물리공격력", self.__물리공격력)
        print("마법공격력", self.__마법공격력)
        print("독립공격력", self.__독립공격력)
        print("크리티컬", self.__크리티컬)
        print("속성강화", self.__속성강화)
        print("스킬 : ", self.__스킬공격력증가)
        print("힘지증 : ", self.__힘_지능_증가)
        print("물마독 : ",self.__물리_마법_독립_공격력증가)
        print("증뎀", self.__증가데미지)
        print("추증뎀",self.__추가증가데미지)
        print("크뎀",self.__크리티컬증가데미지)
        print("추크뎀",self.__추가크리티컬증가데미지)
        print("추뎀",self.__추가데미지)
        print("속성추가데미지", self.__속성추가데미지)
        print("모공",self.__모든공격력증가)
        print("전투력",self.__전투력)
        
    def __str__(self):
        return  "이름 : " +  self.이름 + '\n' + "직업 : " +  self.직업