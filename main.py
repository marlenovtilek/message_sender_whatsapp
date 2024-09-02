import pywhatkit
import os
from dotenv import load_dotenv

load_dotenv()

def send_message():
    mobile = os.getenv('MOBILE')
    message = input('Введите текст сообщения: ')
    hour = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))

    pywhatkit.sendwhatmsg(phone_no=mobile, message=message, time_hour=hour, time_min=minutes) 

def main():
    send_message()


if __name__=='__main__':
    main()
