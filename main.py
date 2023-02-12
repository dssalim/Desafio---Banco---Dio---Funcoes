usuarios = {
  '12345678910': {
    'saldo': 2000.0,
    'agencia': '0001',
    'conta': '001'
  }
}
c = '12345678910'
operacoes_us = [usuarios[c]['saldo']]
saldo_us = [usuarios[c]['saldo']]


def cpf(a):
  b = []
  for i in range(0, len(a)):
    for j in range(0, 10):
      if a[i] == f'{j}': b.append(a[i])
  b = ''.join(b)
  return b


def menu():
  while True:
    print("""Escolha uma operação válida:\n1) Saque \n2) Deposito \n3) Extrato
        """)
    z = int(input())
    if z == 1 or z == 2 or z == 3:
      return z
      continue


def saque(x, saldo):
  if x <= saldo:
    return True
  else:
    return False


def deposito(saldo, x):
  saldo = saldo + x
  return saldo


def extrato():
  extrato = []
  for i in range(0, len(operacoes_us)):
    extrato.append(f'{operacoes_us[i]} \n')
  extrato = ''.join(extrato)
  return extrato


def newop(op):
  if op == "S":
    saldo_us.pop(0)
    caixa()
  else:
    print("Obrigado por usar nossos serviços")


def caixa():
  saldo = saldo_us[0]
  z = menu()
  if z == 1:
    while True:
      print("Informe o valor")
      x = float(input())
      if saque(x, saldo) == True:
        print("Saque Autorrizado")
        saldo = saldo - x
        print(f"Saldo atual é {saldo}")
        operacoes_us.append(saldo)
        print("Deseja realizar outra operação? [s/n]")
        op = input()
        op = op.upper()
        saldo_us.append(saldo)
        operacoes_us.append(newop(op))
        break
      else:
        print(f"Informe um valor válido, seu saldo atual é {saldo}")
  elif z == 2:
    print("informe o valor que deseja depositar")
    x = float(input())
    saldo = deposito(saldo, x)
    print(f'Saldo atual é {saldo}')
    print(saldo_us)
    print("Deseja realizar outra operação? [s/n]")
    op = input()
    op = op.upper()
    saldo_us.append(saldo)
    operacoes_us.append(saldo)
    newop(op)
  elif z == 3:
    print(extrato())
    print("Deseja realizar outra operação? [s/n]")
    op = input()
    op = op.upper()
    saldo_us.append(saldo)
    newop(op)
  else:
    print("informe uma opção valida")
    caixa(saldo)
  return {'saldo': saldo}


def cadastro():
  print("Informe seu cpf para cadastro:\n")
  cpf_1 = str(input())
  cpf_1 = cpf(cpf_1)
  print("Informe seu banco para cadastro:\n")
  banco = str(input())
  print("Informe sua conta para cadastro:\n")
  conta = str(input())
  usuarios[cpf_1] = {'saldo': 0.0, 'agencia': f'{banco}', 'conta': f'{conta}'}
  return cpf_1


def usuario(a):
  if cpf(a) in usuarios.keys():
    return a
  else:
    print("""Usuario não possui cadastro\n
Deseja realizar seu cadastro ou corrigir o CPF informado?[s/n]?\n""")
    d = str(input())
    d = d.strip()
    d = d.upper()
    if d == 'S':
      d = cadastro()
      return d
    else:
      print("obrigado por utilizar nosso serviço")
      exit()


print("""
Informe o seu CPF""")
c = usuario(input())
operacoes_us = [usuarios[c]['saldo']]
saldo_us = [usuarios[c]['saldo']]
usuarios[c]['saldo'] = caixa()

while len(saldo_us) > 1:
  saldo_us.pop(0)
