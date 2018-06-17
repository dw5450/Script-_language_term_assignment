from tkinter import *
from tkinter import font
import tkinter.messagebox


def Tk크기설명(width, height, x, y):
    viewport = str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y)

    return viewport


def Tk글쓰기(Tk, FontSize, FontType, String, xpos, ypos):  # Tk, 폰트 크기, 폰트타입, 입력문자열, (Tk에서의) x위치, y위치
    TempFont = font.Font(Tk, size=FontSize, weight=FontType, family='Consolas')
    MainText = Label(Tk, font=TempFont, text=String)
    MainText.pack()
    MainText.place(x=xpos, y=ypos)


def Tk버튼만들기(Tk, FontSize, FontType, String, Event, xpos, ypos):  # Tk, 폰트 크기, 폰트타입, 입력문자열, 누르면 발생하는 함수,(Tk에서의) x위치, y위치
    TempFont = font.Font(Tk, size=FontSize, weight=FontType, family='Consolas')

    기준캐릭터불러오기버튼 = Button(Tk, font=TempFont, text=String, command=Event)
    기준캐릭터불러오기버튼.pack()
    기준캐릭터불러오기버튼.place(x=xpos, y=ypos)


def Tk입력창만들기(Tk, FontSize, FontType, 폭, xpos, ypos):
    TempFont = font.Font(Tk, size=FontSize, weight=FontType, family='Consolas')
    InputLabel = Entry(Tk, font=TempFont, width=폭)
    InputLabel.pack()
    InputLabel.place(x=xpos, y=ypos)

    return InputLabel


def Tk리스트박스만들기(Tk, FontSize, FontType, StringArr, xpos, ypos):
    ListBoxScrollbar = Scrollbar(Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=xpos + FontSize * 9, y=ypos, width=20, height=FontSize * 2)
    TempFont = font.Font(Tk, size=FontSize, weight=FontType, family='Consolas')
    리스트박스 = Listbox(Tk, font=TempFont, activestyle='none', width=12, height=1, relief='ridge',
                    yscrollcommand=ListBoxScrollbar.set)
    for i in range(len(StringArr)):
        리스트박스.insert(i, StringArr[i])

    리스트박스.pack()
    리스트박스.place(x=xpos, y=ypos)
    ListBoxScrollbar.config(command=리스트박스.yview)

    return 리스트박스


def Tk출력창만들기(Tk, FontSize, width, height, String, xpos, ypos):
    TempFont = font.Font(Tk, size=FontSize, family='Consolas')
    RenderText = Text(Tk, width=width, height=height, relief='ridge')  # yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=xpos, y=ypos)
    # RenderTextScrollbar.config(command=RenderText.yview)
    # RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    RenderText.insert(INSERT, String)

    return RenderText


def Tk라디오버튼만들기(Tk, string, buttonIndex, event, xpos, ypos):
    라디오버튼 = Radiobutton(Tk, text=string, value=buttonIndex, command=event)
    라디오버튼.pack()
    라디오버튼.place(x=xpos, y=ypos)

    return 라디오버튼
