import random
import sys

opciones = ['piedra', 'papel', 'tijera']

if len(sys.argv) != 2 or sys.argv[1] not in opciones:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    sys.exit()

eleccion_computador = random.choice(opciones)

eleccion_usuario = sys.argv[1]

print("Tu jugaste", eleccion_usuario.capitalize())
print("Computador jugó", eleccion_computador.capitalize())

if eleccion_usuario == eleccion_computador:
    print("Empate!")
elif (eleccion_usuario == 'piedra' and eleccion_computador == 'tijera') or \
        (eleccion_usuario == 'papel' and eleccion_computador == 'piedra') or \
        (eleccion_usuario == 'tijera' and eleccion_computador == 'papel'):
    print("Ganaste!!")
else:
    print("Perdiste :(")
