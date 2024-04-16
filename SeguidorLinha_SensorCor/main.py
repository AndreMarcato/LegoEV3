#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor,OUTPUT_B,OUTPUT_C,SpeedPercent,MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
import time

log_on = True

def log(mensagem):
    if log_on:
        arquivo_log.write(mensagem)
        arquivo_log.write("\n")

def sinal(a):
    if a>=0: return 1
    if a<0: return -1

sound = Sound()
sound.speak("E V 3 dev project")

arquivo_log = open('//home//robot//PI_cor.log','a')
log("Inicio arquivo log")

motor_esq = LargeMotor(OUTPUT_B)
motor_dir = LargeMotor(OUTPUT_C)

cor = ColorSensor(INPUT_2)

objetivo = 50
v=50

while True:

    if cor.reflected_light_intensity > objetivo:
        motor_dir.on(v)
        motor_esq.on(0.8*v)
    else:
        motor_dir.on(0.8*v)
        motor_esq.on(v)
  

            
motor_esq.stop()
motor_dir.stop()
sound.beep()


arquivo_log.close()
input("Pressione Enter para encerrar...")