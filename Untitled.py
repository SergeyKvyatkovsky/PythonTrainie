import requests
import smtplib

#r = requests.get('http://httpbin.org/#/Response_formats/get_json')
#print(r.status_code)

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML
from email.mime.image import MIMEImage              # Изображения

addr_to   = "moveton@tut.by" 

def senEmail(addr_to):
    print("&&&&&&&&&&&&&&&&&&" + addr_to)
    addr_from = "skvyatkovsky@clevertec.ru"                 # Адресат
    password  = "qwerTYUI"                                  # Пароль

    msg = MIMEMultipart()                               # Создаем сообщение
    msg['From']    = addr_from                          # Адресат
    msg['To']      = addr_to                            # Получатель
    msg['Subject'] = 'Тема сообщения'                   # Тема сообщения

    body = "Текст сообщения"
    msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

    server = smtplib.SMTP('smtp.yandex.ru', 587)           # Создаем объект SMTP
    server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    server.starttls()                                   # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                   # Получаем доступ
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()                                       # Выходим
    
def noSend():
    print('Ни какого метода тебе')