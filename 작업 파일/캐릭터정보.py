class 캐릭터정보 :
    def __init__(self):
        self.__파싱한정보사전 = None
        self.__캐릭터이름 = ""
        self.__직업 = ""
        self.__힘 = 0
        self.__지능 = 0
        self.__힘_지능_증가 = 0
        self.__물리공격력 = 0
        self.__마법공격력 = 0
        self.__독립공격력 = 0
        self.__물리_마법_독립_공격력증가 = 0
        self.__크리티컬 = 0
        self.__속성강화 = 0#가장 강한 속성만들을 저장
        self.__증가대미지 = 0
        self.__추가증가대미지 = 0
        self.__크리티컬증가대미지 = 0
        self.__추가크리티컬증가대미지 =0
        self.__추가대미지 = 0
        self.__스킬공격력증가 = 0
        self.__기준전투력정보 = 0
        self.__전투력 = 0

        def 전투력계산(self, 기준전투력정보):
            전투력 = 0  # 추후에 c++에서 연동
            return 전투력

    def 캐릭터정보설정하기(self, 캐릭터정보사전):
        pass


        self.__전투력 = self.전투력계산()

    def 캐릭터장비변경(self, 장비타입, 장비이름):
        self.__전투력 = self.전투력계산(기준전투력정보)

    def 출력(self):
        print("이름 : ", self.__캐릭터이름)
        print("직업 : ", self.__직업)
