def Euclides_estendido(a,b):
  """
  Retorna mdc(a,b), x, y tais que a*x + b*y = mdc(a,b)
  Assumimos a,b >= 0 [por enquanto]
  """
  if a == 0:
    return b, 0, 1
  if b == 0:
    return a, 1, 0

  x_anterior = 1
  x_atual = 0
  y_anterior = 0
  y_atual = 1
  Dividendo, Divisor = a, b

  q = 323334641051581231397618509539503/19019684767739993
  print(q)

  while True:
    Quociente, Resto = divmod(Dividendo, Divisor)
    x_anterior, x_atual = x_atual, (x_anterior - x_atual*Quociente)
    y_anterior, y_atual = y_atual, (y_anterior - y_atual*Quociente)
    if Resto == 0:
      return Divisor, x_anterior, y_anterior
    Dividendo, Divisor = Divisor, Resto

print(Euclides_estendido(1828982866109630997434176303059685778909, 1242030202519254059474455275778009437469))