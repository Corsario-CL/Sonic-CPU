# Sonic-CPU - Es un programa que muestra, el uso de la CPU en tiempo real. 
# Desarrollado por CORSARIO_CL
#==========================================================================
import psutil
import time

while True:
    # Obtener el porcentaje de uso de la CPU
    cpu_percent = psutil.cpu_percent()

    # Mostrar el porcentaje de uso de la CPU
    print(f"Uso de la CPU: {cpu_percent}%")

    # Esperar un segundo antes de volver a obtener la información del sistema
    time.sleep(1)
