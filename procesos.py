from pdfminer.high_level import extract_pages, extract_text
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

import time
import threading

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
#Criterio de Arranque: Cada 10 Minuntos Ejecutar Consulta
def timer(timer_runs):
       while timer_runs.is_set():              
             try: 
                    print("timer 1")
                            
             except Exception as error: 
                    print("Error")                     
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
             time.sleep(10)   #ACA SE REGULA EL TIEMPO DE EJECUCION
#---------------------------------------------------------------------------------------------------------------------------------------------------------
def timer1(timer_runs):
       while timer_runs.is_set():              
             try: 
                    print(datetime.now())
                            
             except Exception as error: 
                    print("Error\n")                     
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
             time.sleep(5)   #ACA SE REGULA EL TIEMPO DE EJECUCION  
#---------------------------------------------------------------------------------------------------------------------------------------------------------

#Arrancamos el Sustema Cada Minuntos Despues de Realizar Cada Caso  
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,)) 
h = threading.Thread(target=timer1, args=(timer_runs,)) 
t.start()  
h.start()

  
        
