from playsound import playsound
import datetime

alarm_hour = int(input('What hour do you want the alarm to ring '))
alarm_minute = int(input('What minute do you want the alarm to ring '))
am_pm = input('AM or PM ')

if am_pm == 'pm' or am_pm == 'PM':
    alarm_hour += 12

while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute:
        print('Your alarm is ringing. ')
        playsound("alarm_sound.mp3")
        break