#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor,OUTPUT_B,OUTPUT_C,SpeedPercent,MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# TODO: ADD CODE HERE

sound = Sound()
sound.speak("Welcome to the E V 3 dev project")

# arquivo_log = open('//home//robot//test.log','a')

motor_esq = LargeMotor(OUTPUT_B)
motor_dir = LargeMotor(OUTPUT_C)

sonar = UltrasonicSensor(INPUT_4)
sonar.mode = 'US-DIST-CM'

distancia_alvo = 10.0

while True:
    distancia = sonar.distance_centimeters

    if distancia > 40:
        motor_dir.on(SpeedPercent(100))
        motor_esq.on(SpeedPercent(100))
        # arquivo_log.write("100")
        # arquivo_log("\n")
    elif abs(distancia-distancia_alvo)<=40 and abs(distancia-distancia_alvo)>=0.1:
        maximo = 30
        erro = 100*abs(distancia-distancia_alvo)/maximo
        if distancia-distancia_alvo >=0:
            sinal = 1
        else:
            sinal=-1
        erro = sinal*erro
        motor_dir.on(SpeedPercent(erro))
        motor_esq.on(SpeedPercent(erro))

        # arquivo_log.write(str(erro))
        # arquivo_log.write("\n")
    else:
        motor_esq.stop()
        motor_dir.stop()
        sound.beep()
        # arquivo_log.write("Chegou")
        # arquivo_log.write("\n")
        break


# arquivo_log.close()
input("Pressione Enter para encerrar...")