#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import pygame
class Alarm():
    def __init__(self, hours, minutes, hours_2, minutes_2, hours_3, minutes_3, hours_4, minutes_4, hours_5, minutes_5, \
                 hours_6, minutes_6, hours_7, minutes_7, hours_8, minutes_8, hours_9, minutes_9, hours_10, minutes_10, \
                 hours_11, minutes_11, hours_12, minutes_12, hours_13, minutes_13, hours_14, minutes_14, hours_15, minutes_15, \
                 hours_16, minutes_16, hours_17, minutes_17, music_time):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.hours_2 = int(hours_2)
        self.minutes_2 = int(minutes_2)
        self.hours_3 = int(hours_3)
        self.minutes_3 = int(minutes_3)
        self.hours_4 = int(hours_4)
        self.minutes_4 = int(minutes_4)
        self.hours_5 = int(hours_5)
        self.minutes_5 = int(minutes_5)
        self.hours_6 = int(hours_6)
        self.minutes_6 = int(minutes_6)
        self.hours_7 = int(hours_7)
        self.minutes_7 = int(minutes_7)
        self.hours_8 = int(hours_8)
        self.minutes_8 = int(minutes_8)
        self.hours_9 = int(hours_9)
        self.minutes_9 = int(minutes_9)
        self.hours_10 = int(hours_10)
        self.minutes_10 = int(minutes_10)
        self.hours_11 = int(hours_11)
        self.minutes_11 = int(minutes_11)
        self.hours_12 = int(hours_12)
        self.minutes_12 = int(minutes_12)
        self.hours_13 = int(hours_13)
        self.minutes_13 = int(minutes_13)
        self.hours_14 = int(hours_14)
        self.minutes_14 = int(minutes_14)
        self.hours_15 = int(hours_15)
        self.minutes_15 = int(minutes_15)
        self.hours_16 = int(hours_16)
        self.minutes_16 = int(minutes_16)
        self.hours_17 = int(hours_17)
        self.minutes_17 = int(minutes_17)
        self.music_time = int(music_time)
        self.fadeout = 2000
        self.keep_running = True

    def run(self):

            while True:
                now = time.localtime()
                if ((now.tm_hour == self.hours and now.tm_min == self.minutes)\
                        or (now.tm_hour == self.hours_2 and now.tm_min == self.minutes_2)\
                        or (now.tm_hour == self.hours_3 and now.tm_min == self.minutes_3)\
                        or (now.tm_hour == self.hours_4 and now.tm_min == self.minutes_4)\
                        or (now.tm_hour == self.hours_5 and now.tm_min == self.minutes_5)\
                        or (now.tm_hour == self.hours_6 and now.tm_min == self.minutes_6)\
                        or (now.tm_hour == self.hours_7 and now.tm_min == self.minutes_7)\
                        or (now.tm_hour == self.hours_8 and now.tm_min == self.minutes_8)\
                        or (now.tm_hour == self.hours_9 and now.tm_min == self.minutes_9)\
                        or (now.tm_hour == self.hours_10 and now.tm_min == self.minutes_10)\
                        or (now.tm_hour == self.hours_11 and now.tm_min == self.minutes_11)\
                        or (now.tm_hour == self.hours_12 and now.tm_min == self.minutes_12)\
                        or (now.tm_hour == self.hours_13 and now.tm_min == self.minutes_13)\
                        or (now.tm_hour == self.hours_14 and now.tm_min == self.minutes_14)\
                        or (now.tm_hour == self.hours_15 and now.tm_min == self.minutes_15)\
                        or (now.tm_hour == self.hours_16 and now.tm_min == self.minutes_16)\
                        or (now.tm_hour == self.hours_17 and now.tm_min == self.minutes_17)):
                    print("BELL TIME!!!")
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("music.wav")
                    sound.play()
                    time.sleep(self.music_time-(int(self.fadeout/1000)))
                    sound.fadeout(self.fadeout)
                    print("Waiting fot the next alarm at: "+str(self.hours)+" : "+str(self.minutes))
                    time.sleep(60)


#Main execution
def main():
    #zilin calma uzunlugu
    music_time= 5
    #sinifa gidis
    alarm_HH = 16
    alarm_MM = 3
    print("You'll be saved by the bell at: " + str(alarm_HH) +" : "+ str(alarm_MM))


    #ders 1 baslangic
    alarm_HH_2 = 16
    alarm_MM_2 = 4
    print("You'll be saved by the second bell at: " + str(alarm_HH_2) +" : "+ str(alarm_MM_2))

    #ders 2 baslangic
    alarm_HH_3 = 1
    alarm_MM_3 = 12
    print("You'll be saved by the third bell at: " + str(alarm_HH_3) +" : "+ str(alarm_MM_3))

    #ders 3 baslangic
    alarm_HH_4 = 1
    alarm_MM_4 = 13
    print("You'll be saved by the third bell at: " + str(alarm_HH_4) +" : "+ str(alarm_MM_4))

    #ders 4 baslangic
    alarm_HH_5 = 1
    alarm_MM_5 = 14
    print("You'll be saved by the third bell at: " + str(alarm_HH_5) +" : "+ str(alarm_MM_5))

    #teneffus 1 baslangic
    alarm_HH_6 = 1
    alarm_MM_6 = 15
    print("You'll be saved by the third bell at: " + str(alarm_HH_6) +" : "+ str(alarm_MM_6))

    #teneffus 1 den sinifa donus
    alarm_HH_7 = 1
    alarm_MM_7 = 16
    print("You'll be saved by the third bell at: " + str(alarm_HH_7) +" : "+ str(alarm_MM_7))

    #ders 5
    alarm_HH_8 = 1
    alarm_MM_8 = 17
    print("You'll be saved by the third bell at: " + str(alarm_HH_8) +" : "+ str(alarm_MM_8))

    #ders 6
    alarm_HH_9 = 1
    alarm_MM_9 = 18
    print("You'll be saved by the third bell at: " + str(alarm_HH_9) +" : "+ str(alarm_MM_9))

    #ders 7
    alarm_HH_10 = 1
    alarm_MM_10 = 19
    print("You'll be saved by the third bell at: " + str(alarm_HH_10) +" : "+ str(alarm_MM_10))

    #ders 8
    alarm_HH_11 = 1
    alarm_MM_11 = 20
    print("You'll be saved by the bell at: " + str(alarm_HH_11) +" : "+ str(alarm_MM_11))


    #teneffus 2 baslangic
    alarm_HH_12 = 1
    alarm_MM_12 = 21
    print("You'll be saved by the second bell at: " + str(alarm_HH_12) +" : "+ str(alarm_MM_12))

    #teneffus 2 den sinifa donus
    alarm_HH_13 = 1
    alarm_MM_13 = 21
    print("You'll be saved by the third bell at: " + str(alarm_HH_13) +" : "+ str(alarm_MM_13))

    #ders 9 baslangic
    alarm_HH_14 = 1
    alarm_MM_14 = 23
    print("You'll be saved by the third bell at: " + str(alarm_HH_14) +" : "+ str(alarm_MM_14))

    #ders 10 baslangic
    alarm_HH_15 = 1
    alarm_MM_15 = 24
    print("You'll be saved by the third bell at: " + str(alarm_HH_15) +" : "+ str(alarm_MM_15))

    #ders 11 baslangic
    alarm_HH_16 = 1
    alarm_MM_16 = 25
    print("You'll be saved by the third bell at: " + str(alarm_HH_16) +" : "+ str(alarm_MM_16))

    #eve gitme vakti
    alarm_HH_17 = 1
    alarm_MM_17 = 26
    print("You'll be saved by the third bell at: " + str(alarm_HH_17) +" : "+ str(alarm_MM_17))

    alarm = Alarm(alarm_HH, alarm_MM, alarm_HH_2, alarm_MM_2, alarm_HH_3, alarm_MM_3, alarm_HH_4, alarm_MM_4,\
                  alarm_HH_5,alarm_MM_5, alarm_HH_6, alarm_MM_6, alarm_HH_7, alarm_MM_7, alarm_HH_8, alarm_MM_8,\
                  alarm_HH_9, alarm_MM_9, alarm_HH_10, alarm_MM_10, alarm_HH_11, alarm_MM_11, alarm_HH_12, alarm_MM_12,\
                  alarm_HH_13, alarm_MM_13, alarm_HH_14, alarm_MM_14, alarm_HH_15, alarm_MM_15, alarm_HH_16, alarm_MM_16,\
                  alarm_HH_17, alarm_MM_17, music_time)
    alarm.run()



if __name__ == "__main__":
 main()
