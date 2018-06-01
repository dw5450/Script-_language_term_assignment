from 던파API파싱하기 import *
from 캐릭터정보 import *

from tkinter import *
from tkinter import font
import tkinter.messagebox

def getViewport(width, height,x , y):

    viewport = str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y)

    return viewport

class 던파스카우터프레임워크:
    def __init__(self):

        
        self.메뉴_Tk = Tk()
        self.root_Tk_x = 600
        self.root_Tk_y = 200
        self.root_Tk_width = 205
        self.root_Tk_height = 200
        self.메뉴_Tk.geometry(getViewport(self.root_Tk_width, self.root_Tk_height, self.root_Tk_x, self.root_Tk_y))
        self.drawedTk = self.메뉴_Tk

        self.AppState = '메뉴' #'기본캐릭터불러오기' # '측정캐릭터불러오기' # '측정캐릭아이템변경 #측정캐릭터측정하기

        self.기준캐릭터불러오기_Tk = None


        self.__loopFlag = True
        self.__xmlFD = -1
        self.__고인물전투력 = {'독립공격력' : 762652.38, "물리,마법공격력" : 7623841.0}
        self.__노오력전투력 = {'독립공격력': 146841.49, "물리,마법공격력": 1466123.27}
        self.__퀘전전투력 = {'독립공격력': 20583.06, "물리,마법공격력": 206496.24}
        self.__출력타입 = '독립공격력'
        self.__찾는서버 = None
        self.__찾는이름 = None
        self.__기준캐릭터 = None
        self.__측정캐릭터 = 캐릭터정보()

    def SearchButtonAction(self):
        global SearchListBox
        global InputLabel
        global RenderText
        RenderText.configure(state='normal')
        RenderText.delete(0.0, END)
        iSearchIndex = SearchListBox.yview()[0]
        iSearchIndex = int(iSearchIndex * 8)
        print(iSearchIndex)
        if(iSearchIndex == 0):
            self.__찾는서버 = '카인'
        elif (iSearchIndex == 1):
            self.__찾는서버 = '디레지에'
        elif (iSearchIndex == 2):
            self.__찾는서버 = '시로코'
        elif (iSearchIndex == 3):
            self.__찾는서버 = '프레이'
        elif (iSearchIndex == 4):
            self.__찾는서버 = '카시야스'
        elif (iSearchIndex == 5):
            self.__찾는서버 = '힐더'
        elif (iSearchIndex == 6):
            self.__찾는서버 = '안톤'
        elif (iSearchIndex == 7):
            self.__찾는서버 = '바칼'

        찾는이름 = InputLabel.get()
        공격유형 = '독립공격력'

        if 찾는이름 != self.__찾는이름:
            self.__찾는이름 = 찾는이름
            self.__측정캐릭터.캐릭터가져오기(self.__찾는서버 , 찾는이름, 공격유형)
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "캐릭터이름 : ")
            RenderText.insert(INSERT, self.__측정캐릭터.캐릭터이름)
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
            if(self.__출력타입 == '독립공격력'):
                RenderText.insert(INSERT, int(self.__측정캐릭터.전투력가져오기()/self.__고인물전투력['독립공격력'] * 100)/100)
                RenderText.insert(INSERT, " 고인물 ")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, int(self.__측정캐릭터.전투력가져오기()/self.__노오력전투력['독립공격력'] * 100)/100)
                RenderText.insert(INSERT, " 노오력")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, int(self.__측정캐릭터.전투력가져오기() / self.__퀘전전투력['독립공격력'] * 100)/100)
                RenderText.insert(INSERT, " 퀘전")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")
            else:
                RenderText.insert(INSERT, int(self.__측정캐릭터.전투력가져오기() / self.__고인물전투력['물리,마법공격력'] * 100) / 100)
                RenderText.insert(INSERT, " 고인물 ")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, int(self.__측정캐릭터.전투력가져오기() / self.__노오력전투력['물리,마법공격력'] * 100) / 100)
                RenderText.insert(INSERT, " 노오력")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, int(self.__측정캐릭터.전투력가져오기() / self.__퀘전전투력['물리,마법공격력'] * 100) / 100)
                RenderText.insert(INSERT, " 퀘전")
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")


    ## GUI의 제목을 탑에다 적자

    def 앱상태기준캐릭터불러오기(self):

        self.기준캐릭터불러오기Tk = Tk()
        self.기준캐릭터불러오기Tk.geometry(getViewport(self.root_Tk_width, self.root_Tk_height, self.root_Tk_x, self.root_Tk_y))
        self.InitSearchListBox()
        self.drawedTk = self.기준캐릭터불러오기Tk

    def 앱상태측정캐릭터불러오기(self):
        self.AppState = '측정캐릭터불러오기'

    def 앱상태측정캐릭터아이템변경(self):
        self.AppState = '측정캐릭터아이템변경'

    def 앱상태측정캐릭터측정하기(self):
        self.AppState = '측정캐릭터측정하기'




    def RootAppTopText(self):
        TempFont = font.Font(self.메뉴_Tk, size=20, weight='bold', family='Consolas')
        MainText = Label(self.메뉴_Tk, font=TempFont, text="[던파스카우터!]")
        MainText.pack()
        MainText.place(x=0, y=0)

    def RootAppButton(self):
        TempFont = font.Font(self.메뉴_Tk, size=14, weight='bold', family='Consolas')

        기준캐릭터불러오기버튼 = Button(self.메뉴_Tk, font=TempFont, text="기준 캐릭터 불러오기", command=self.앱상태기준캐릭터불러오기)
        기준캐릭터불러오기버튼.pack()
        기준캐릭터불러오기버튼.place(x=0, y=40)

        TempFont = font.Font(self.메뉴_Tk, size=14, weight='bold', family='Consolas')

        측정캐릭터불러오기버튼 = Button(self.메뉴_Tk, font=TempFont, text="측정 캐릭터 불러오기", command=self.앱상태측정캐릭터불러오기)
        측정캐릭터불러오기버튼.pack()
        측정캐릭터불러오기버튼.place(x=0, y=80)

        TempFont = font.Font(self.메뉴_Tk, size=14, weight='bold', family='Consolas')

        측정캐릭터아이템변경버튼 = Button(self.메뉴_Tk, font=TempFont, text="측정 캐릭 아이템변경", command=self.앱상태측정캐릭터아이템변경)
        측정캐릭터아이템변경버튼.pack()
        측정캐릭터아이템변경버튼.place(x=0, y=120)

        TempFont = font.Font(self.메뉴_Tk, size=14, weight='bold', family='Consolas')

        측정캐릭터아이템변경버튼 = Button(self.메뉴_Tk, font=TempFont, text="측정 캐릭터 측정하기", command=self.앱상태측정캐릭터측정하기)
        측정캐릭터아이템변경버튼.pack()

        측정캐릭터아이템변경버튼.place(x=0, y=160)

    def InitSearchListBox(self):
        global SearchListBox
        TempFont = font.Font(self.메뉴_Tk, size=15, weight='bold', family='Consolas')
        MainText = Label(self.메뉴_Tk, font=TempFont, text="서버 ")
        MainText.pack()
        MainText.place(x=self.root_Tk_width, y=100)

        ListBoxScrollbar = Scrollbar(self.메뉴_Tk)
        ListBoxScrollbar.pack()
        ListBoxScrollbar.place(x=self.root_Tk_x + self.root_Tk_width, y=90)
        SearchListBox = Listbox(self.메뉴_Tk, font=TempFont, activestyle='none',
                                width=10, height=1, borderwidth=12, relief='ridge',
                                yscrollcommand=ListBoxScrollbar.set)

        SearchListBox.insert(1, "카인")
        SearchListBox.insert(2, "디레지에")
        SearchListBox.insert(3, "시로코")
        SearchListBox.insert(4, "프레이")
        SearchListBox.insert(5, "카시야스")
        SearchListBox.insert(6, "힐더")
        SearchListBox.insert(7, "안톤")
        SearchListBox.insert(8, "바칼")
        SearchListBox.pack()
        print(self.root_Tk_x)
        SearchListBox.place(x=self.root_Tk_width, y=90)
        ListBoxScrollbar.config(command=SearchListBox.yview)

    def InitInputLabel(self):
        global InputLabel
        TempFont = font.Font(self.메뉴_Tk, size=15, weight='bold', family='Consolas')
        MainText = Label(self.메뉴_Tk, font=TempFont, text="이름 ")
        MainText.pack()
        MainText.place(x=10, y=155)

        InputLabel = Entry(self.메뉴_Tk, font=TempFont, width=15, borderwidth=12, relief='ridge')
        InputLabel.pack()
        InputLabel.place(x=70, y=145)

    def InitSearchButton(self):
        TempFont = font.Font(self.메뉴_Tk, size=12, weight='bold', family='Consolas')
        SearchButton = Button(self.메뉴_Tk, font=TempFont, text="검색", command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=330, y=100)

    def InitRenderText(self):
        global RenderText

        #RenderTextScrollbar = Scrollbar(self.메뉴_Tk)
        #RenderTextScrollbar.pack()
        #RenderTextScrollbar.place(x=375, y=220)

        TempFont = font.Font(self.메뉴_Tk, size=10, family='Consolas')
        RenderText = Text(self.메뉴_Tk, width=49, height=23, borderwidth=12,
                          relief='ridge') #yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=235)
        #RenderTextScrollbar.config(command=RenderText.yview)
        #RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

        RenderText.configure(state='disabled')

    def __측정_캐릭터_설정하기(self):
        pass


    def 실행하기(self):
        if self.AppState == '메뉴':
            self.RootAppTopText()
            self.RootAppButton()

        self.drawedTk.mainloop()


fw = 던파스카우터프레임워크()
fw.실행하기()