from pickle import FALSE, TRUE



def contarseniaValida (contrasenia):
    if (contrasenia=='2Fj(jjbFsuj') or (contrasenia=='eoZiugBf&g9'):
      return True
    else:
      return False

if __name__== '__main__':

  print(contarseniaValida("2Fj(jjbFsuj"))
  print(contarseniaValida("eoZiugBf&g9"))
  print(contarseniaValida(125))
  print(contarseniaValida(1.1))