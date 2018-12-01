import serial
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1.0) 

# /dev/ttyACM0 se modifica según el puerto que se esté utilizando (COM3)
# baudurate equivale a 

