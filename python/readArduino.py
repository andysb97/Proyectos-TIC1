import time
import warnings
from collections import deque #dequeue
import serial #conecta con arduino a través de ASCII
import numpy
import matplotlib.pyplot as plt #grafica

# para registrar los eventos durante 1 hora
num = 60  

# deque con longitud máxima 60 para temperatura, humedad ambiente y suelo
data_temp = deque([0] * num, maxlen=num)  
data_hamb = deque([0] * numb, maxlen=num) 
data_hs = deque([0] * num, maxlen=num)    

#Creamos la figura (gráfico)
plt.ion()                     #activa la figura para procesar datos
figure, axes = plt.subplots() #
ll, = ax.plot(data_temp)      #

# Abrimos la conexión con Arduino
    # '/dev/ttyACM0' equivale al puerto de conexión COM3
    # baudrate equivale begin.serial()
    # timeout equivale delay(1000)
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1.0)
arduino.setDTR(False)
time.sleep(1)
arduino.flushInput()
arduino.setDTR(True)

with arduino:
    while True:
        try:
            line = arduino.readline()
            if not line:
                # HACK: Descartamos líneas vacías porque fromstring produce
                # resultados erróneos, ver
                # https://github.com/numpy/numpy/issues/1714
                continue
            xx, yy = np.fromstring(line.decode('ascii', errors='replace'),
                                   sep=' ')
            data.append(yy)
            ll.set_ydata(data)
            ax.set_ylim(min(data) - 10, max(data) + 10)
            plt.pause(0.001)
        except ValueError:
            warnings.warn("Line {} didn't parse, skipping".format(line))
        except KeyboardInterrupt:
            print("Exiting")
            break

