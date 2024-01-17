
import random

def generar_nombre_silly ():
    
    nombre = ['beto','churro','flaco','andres','mes','arture']
    sustantivos = ['Cucharón','Calcetín',' Pepinillo','Sillón', 'Tocineta']
    
    nombre = random.choice(nombre)
    sustantivo= random.choice(sustantivos)
    
    return f'{nombre}{sustantivo}'

nombre_divertido=generar_nombre_silly()
print(f'tu nombre divertido es: {nombre_divertido}')

while True:

  


    respuesta = input('¿Quieres generar otro nombre? (sí/no): ')
    if respuesta.lower() != 'sí':
        break  