import sys
# Punto 1
peso = float(sys.argv[1])
altura_cm = float(sys.argv[2])

altura_m = altura_cm / 100

# Punto 2
imc = peso / (altura_m ** 2)


clasificacion = ""
if imc < 18.5:
    clasificacion = "Bajo Peso"
elif 18.5 <= imc < 25:
    clasificacion = "Adecuado"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
elif 30 <= imc < 35:
    clasificacion = "Obesidad Grado I"
elif 35 <= imc < 40:
    clasificacion = "Obesidad Grado II"
else:
    clasificacion = "Obesidad Grado III"
    
# Punto 3
print("Su IMC es {:.2f}".format(imc))
print("La clasificación OMS es", clasificacion)
