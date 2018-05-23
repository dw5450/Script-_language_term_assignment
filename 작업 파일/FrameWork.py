
class FrameWork:
    def __init__(self):
        self.__loopFlag = 1
        self.__xmlFD = -1
        self.__기준캐릭터사전 = None
        self.__비교캐릭터사전 = None

    def __printMenu(self):
        print("     던파 스카우터!     ")
        print("========Menu==========")
        print("기준 캐릭터 설정하기 : q")
        print("측정 캐릭터 가져오기 : w")
        print("측정 캐릭터 설정하기 : e")
        print("측정 캐릭터 출력하기 : r")
        print("     종료하기      : z")
        print("==================")


    def __기준_캐릭터_설정하기(self):
        pass

    def __측정_캐릭터_가져오기(self):
        pass

    def __측정_캐릭터_설정하기(self):
        pass

    def __측정_캐릭터_출력하기(self):
        pass

    def launcherFunction(self, menu):
        if menu == 'q':
            self.__기준_캐릭터_설정하기()
        elif menu == 'w':
            self.__측정_캐릭터_가져오기()
        elif menu == 'e':
            self.__측정_캐릭터_설정하기()
        elif menu == 'r':
            self.__측정_캐릭터_출력하기()
        elif menu == 'z':
            self.__loopFlag = 0 #종료하기
        else:
            print("error : 설정 된 키값이 아닙니다. capslock이나 한글 설정을 확인해주세요.")

    def Active(self):
        while(self.loopFlag > 0):
            self.__printMenu()
            menuKey = str(input ('메뉴 선택하기   :  '))
            self.__launcherFunction(menuKey)
        else:
            print ("프로그램을 이용해 주셔서 감사합니다.")