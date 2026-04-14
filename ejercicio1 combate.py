def calcular_dano(ataque, defensa):
    dano = ataque - defensa
    if dano < 0:
        return 0
    return dano
 

def aplicar_dano(hp_actual, dano):
    nuevo_hp = hp_actual - dano
    if nuevo_hp < 0:
        return 0
    return nuevo_hp

def mostrar_estado(nombre, hp, hp_max=100):
    print(f"{nombre}: {hp}/{hp_max}")

def realizar_ataque(atacante, defensor, dano):
    print(f"{atacante} ataca a {defensor} por {dano} de daño")

hp_heroe = 100
hp_enemigo = 50

print("estado inicial:")
mostrar_estado("heroe", hp_heroe)
mostrar_estado("enemigo", hp_enemigo) 


dano = calcular_dano(ataque=25, defensa=10)
realizar_ataque("heroe", "enemigo", dano)
hp_enemigo = aplicar_dano(hp_enemigo, dano)
mostrar_estado("enemigo", hp_enemigo)

realizar_ataque("heroe", "enemigo", dano)
hp_enemigo = aplicar_dano(hp_enemigo, dano)
mostrar_estado("enemigo", hp_enemigo)
