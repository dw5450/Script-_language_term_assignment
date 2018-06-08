# -*- coding: utf-8 -*-

import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value

def SendMail(MailAdress,info_text):
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "logo.html"

    senderAddr = "aw13dw5450@gmail.com"     # 보내는 사람 email 주소.
    recipientAddr = MailAdress   # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "던파스카우터! 정보 이메일"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    #htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(info_text,'html', _charset = 'UTF-8' )
    #htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = smtplib.SMTP("smtp.gmail.com",port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr,"aw1323qe")
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()

