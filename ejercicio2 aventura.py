import random 
from datetime import *

def generar_nombre():
    nombres = ["Matias", "Maria", "Pedro", "Jose"]
    return random.choice(nombres)

def generar_clase():
    clase = ["guerrero", "mago", "bruja", "soldado"]
    return random.choice(clase)

def generar_hp():
    return random.randint(80, 120)

def mostrar_fecha():
    fecha = datetime.now()
    print(f" {fecha.day}/{fecha.month}/{fecha.year}")


print("Generador de aventuras:")
mostrar_fecha()

print("heroes generados:")
nombre = generar_nombre()
clase = generar_clase()
hp = generar_hp()
print(f"Heroe: {nombre} / Clase: {clase}  / HP: {hp}")


nombre = generar_nombre()
clase = generar_clase()
hp = generar_hp()
print(f"Heroe: {nombre} / Clase: {clase}  / HP: {hp}")

nombre = generar_nombre()
clase = generar_clase()
hp = generar_hp()
print(f"Heroe: {nombre} / Clase: {clase}  / HP: {hp}")
