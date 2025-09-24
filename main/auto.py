import pydirectinput
import time

pydirectinput.PAUSE = 0

'''fim = time.time() + 0.1
while time.time() < fim:
    pydirectinput.press('e')
   '''
   
   
""" FAIXA 1 - VOLTA """

time.sleep(2)

def repetir_sequencia(vezes):
    for i in range(vezes):
        print(f"Executando sequencia {i+1}/{vezes}...")

        pydirectinput.keyDown('e')
        time.sleep(1.5)
        pydirectinput.keyUp('e') 

        time.sleep(1)

        pydirectinput.keyDown('w')
        time.sleep(3.2)
        pydirectinput.keyUp('w')   
        
time.sleep(2)
repetir_sequencia(4)



