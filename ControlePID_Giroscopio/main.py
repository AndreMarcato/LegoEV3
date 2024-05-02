#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor,OUTPUT_B,OUTPUT_C,SpeedPercent,MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor,GyroSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
import time, csv

log_on = True

if log_on:
    
    arquivo_csv = open('//home//robot//PI_giro.csv','w',newline='')
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Tempo', 'P', 'I', 'D'])
    log_data = {"tempo": [], "P": [], "I": [], "D": []}
    
    def log(mensagem):

        escritor_csv.writerow(mensagem[:])
        
def girar(velocidade):
    motor_dir.on(-velocidade)
    motor_esq.on(velocidade)

def sinal(a):
    if a>=0: return 1
    if a<0: return -1
        
def dt():
    return time.time()-t

sound = Sound()
sound.speak("E V 3 dev project")


log("Inicio arquivo log")

motor_esq = LargeMotor(OUTPUT_B)
motor_dir = LargeMotor(OUTPUT_C)

giro = GyroSensor(INPUT_2)
giro.mode = giro.MODE_GYRO_ANG
giro.reset()

angulo_alvo = 45
tol = 1

kp = 10
ki = 1
kd = 0

I=0

t=time.time()
ti=t

while abs(angulo_alvo-giro.angle)>tol:

    erro_angulo = 100*(angulo_alvo-giro.angle)/360
    
    P = kp*erro_angulo
    I = I + ki*erro_angulo*dt()
    D = kd*erro_angulo/dt()
    u = P+I+D
    
    if abs(u)>100: u=sinal(u)*100
    
    girar(u)
    t = time.time()

  

            
motor_esq.stop()
motor_dir.stop()
sound.beep()


arquivo_log.close()
input("Pressione Enter para encerrar...")