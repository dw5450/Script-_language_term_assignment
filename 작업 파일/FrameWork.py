from 던파API파싱하기 import *
from 캐릭터정보 import *

class 던파스카우터프레임워크:
    def __init__(self):
        self.__loopFlag = True
        self.__xmlFD = -1
        self.__기준캐릭터_퀘전 = None
        self.__기준캐릭터_노오력 = None
        self.__기준캐릭터_모인물 = None
        self.__기준캐릭터 = None
        self.__측정캐릭터 = None

    def __캐릭터가져오기(self):
        임시캐릭터 = 캐릭터정보()
        서버이름 = input("가져오실 캐릭터의 서버를 입력해주세요 : ")
        캐릭터이름 = input("가져오실 캐릭터의 이름을 입력해주세요 : ")
        공격타입 = input("가져오실 캐릭터의 공격타입를 입력해주세요 : ")
        임시캐릭터.캐릭터가져오기(서버이름, 캐릭터이름, 공격타입)

        return 임시캐릭터

    def __printMenu(self):
        print("     던파 스카우터!     ")
        print("========Menu==========")
        print("기준 캐릭터 설정하기 : q")
        print("측정 캐릭터 가져오기 : w")
        print("측정 캐릭터 설정하기 : e")
        print("측정 캐릭터 출력하기 : r")
        print("     종료하기      : z")
        print("======================")


    def __기준_캐릭터_설정하기(self):
        print("어떤 설정을 이용하실 건가요?")
        print("설정 캐릭터 사용하기 : q")
        print("서버에서 불러오기 : w")

        선택 = str(input ('선택하기   :  '))

        if(선택 =='q'):
            print("어떤 설정을 이용하실 건가요?")
            print("1. 퀘전  2. 노오오력  3. 모인물")
            선택 = str(input('선택하기   :  '))
            pass

        elif(선택 == 'w'):
           self. __기준캐릭터 = self.__캐릭터가져오기()

        else:
            print("설정되지 않은 입력입니다.")


    def __측정_캐릭터_가져오기(self):
        self.__측정캐릭터 = self.__캐릭터가져오기()

    def __측정_캐릭터_설정하기(self):
        pass

    def __측정_캐릭터_출력하기(self):
        if(self.__측정캐릭터 !=  None or self.__측정캐릭터 != False):
            self.__측정캐릭터.출력()

    def __launcherFunction(self, menu):
        if menu == 'q':
            self.__기준_캐릭터_설정하기()
        elif menu == 'w':
            self.__측정_캐릭터_가져오기()
        elif menu == 'e':
            self.__측정_캐릭터_설정하기()
        elif menu == 'r':
            self.__측정_캐릭터_출력하기()
        elif menu == 'z':
            self.__loopFlag = False #종료하기
        else:
            print("error : 설정 된 키값이 아닙니다. capslock이나 한글 설정을 확인해주세요.")


    def 실행하기(self):
        while(self.__loopFlag > 0):
            self.__printMenu()
            menuKey = str(input ('메뉴 선택하기   :  '))
            self.__launcherFunction(menuKey)
        else:
            print ("프로그램을 이용해 주셔서 감사합니다.")



fw = 던파스카우터프레임워크()
fw.실행하기()