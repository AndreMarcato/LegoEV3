#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor,OUTPUT_B,OUTPUT_C,SpeedPercent,MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor,GyroSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.button import Button
import time, csv

btn = Button()

print("Seta direita: log_on true")
print("Seta esquerda: log_on false")

btn.wait_for_bump()
if btn.right:
    log_on = True
elif btn.left:
    log_on = False  



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
        

sound = Sound()
sound.beep()

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

dt = 0
I=0

t=time.time()
ti=t

while abs(angulo_alvo-giro.angle)>tol:

    erro = 100*(angulo_alvo-giro.angle)/360
    
    dt = time.time() - t
    
    P = kp*erro
    I = I + ki*erro*dt
    D = kd*erro/dt
    u = P+I+D
    
    u = sinal(erro)*max(u,100)
    
    if log_on:
        log_data["tempo"].append(t-ti)
        log_data["P"].append(P)
        log_data["I"].append(I)
        log_data["D"].append(D)

    t = time.time()
    
    girar(u)
    
for i in range(len(log_data["tempo"])):
 
    log([log_data['tempo'][i],log_data['P'][i],log_data['I'][i],log_data['D'][i]])
              
motor_esq.stop()
motor_dir.stop()
sound.beep()


arquivo_csv.close()
input("Pressione Enter para encerrar...")