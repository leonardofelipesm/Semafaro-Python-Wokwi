from machine import Pin
from time import ticks_ms, sleep
#estado : 0->verde, 1->amarelo, 2->vermelho

led = (Pin (14, Pin.OUT),
       Pin (13, Pin.OUT),
       Pin (12, Pin.OUT),
       Pin (18, Pin.OUT),
       Pin (19, Pin.OUT))

tempo = (5000,
         1500,
         3000)

botao = Pin(5, Pin.IN, Pin.PULL_DOWN)

estado = 0
futuro = ticks_ms()

while True:
        if ticks_ms() - futuro > 0:
            led[estado].off()
            if estado < 2:
                estado = estado + 1
            else:
                estado = 0
            led[estado].on()

            if estado == 2:
              led[3].on()
              led[4].off()
            else :
              led[4].on()
              led[3].off()

            futuro = ticks_ms() + tempo[estado]

        if botao.value() == 1:
            if estado == 0:
                futuro = ticks_ms() + 1000
            sleep(0.3)
                

