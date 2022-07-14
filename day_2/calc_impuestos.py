def calcularImpuestos(edad, ingresos):
  if edad >= 18 and ingresos >= 1000:
    return int(ingresos*0.4)
  else:
    return 0

if __name__== '__main__':

  print(calcularImpuestos(18, 1000))
  print(calcularImpuestos(40, 10000))
