
def bmi (peso, altura):
  bmi = altura**2
  bmi = round (peso / bmi,2)
  if bmi < 18.5:
    print(bmi)
    return ('Peso bajo')

  elif bmi >= 18.5 and bmi <= 24.9:
    print(bmi)
    return ('Normal')
  
  elif bmi >= 25 and bmi <= 29.9:
    print(bmi)
    return ('Sobrepeso')
  
  elif bmi >= 30:
    print(bmi)
    return ('Obeso')
  else:
    return 0

if __name__== '__main__':

  bmi(65, 1.8)
  bmi(72, 1.6)
  bmi(52, 1.75)
  bmi(135, 1.7)