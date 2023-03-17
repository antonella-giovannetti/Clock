import time
import datetime
import keyboard

hour_now = (16, 59, 59)
hour_alarm = (17, 1, 0)

def choose_format_hour():
    while True:
        print('Choissisez le format de l\'heure : ')
        print('1 - Format de 24h')
        print('2 - Format de 12h')
        number = input('> ')
        if number.isdigit() == False:
                print(' ')
                print('Veuillez entrer un chiffre entre 1 et 3!')
                print(' ')
        elif number == "1":
            display_time(hour_now, 24)
        elif number == "2":
            display_time(hour_now, 12)
        else:
            print('Veuillez entrer un chiffre valide')

def display_time(hour, format):
    hour_list = list(hour)
    while True:
        hour_list[2] += 1
        if hour_list[2] == 60:
            hour_list[2] = 0
            hour_list[1] += 1
            if hour_list[1] == 60:
                hour_list[1] = 0
                hour_list[0] += 1
                if hour_list[0] == 24:
                    hour_list[0] = 0
        if format == 24:
            hour_format = format_24((hour_list[0], hour_list[1], hour_list[2]))
            hour_alarm_format = format_24((hour_alarm[0], hour_alarm[1], hour_alarm[2]))
        elif format == 12:
            hour_format = format_12((hour_list[0], hour_list[1], hour_list[2]))
            hour_alarm_format = format_12((hour_alarm[0], hour_alarm[1], hour_alarm[2]))
        print(hour_format, end='\r')
        alarm(hour_alarm_format, hour_format)
        time.sleep(1)

def alarm(hour_alarm, hour):
    if(hour_alarm == hour):
        print('L\'ALARME SONNE')

def format_12(hour):
    hour_list = list(hour)
    hour_datetime = datetime.datetime(2000, 1, 1, hour_list[0], hour_list[1], hour_list[2])
    hour_format = hour_datetime.strftime('%I:%M:%S %p')
    return hour_format

def format_24(hour):
    hour_list = list(hour)
    hour_format = datetime.time(hour_list[0], hour_list[1], hour_list[2])
    return hour_format

# def pause(): 
#     while True:
#         if keyboard.read_key() == "p":
#             print("You pressed p")
#             break
# pause()
choose_format_hour()
