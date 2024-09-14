valor = 0

while True:
    option = input("Selecione uma opção \n 1 - depositar \n 2 - sacar \n 0 - sair")
    if int(option) == 0:
        break
    if int(option) == 1:
        deposito = input("Digite o valor que deseja depositar")
        valor = valor + float(deposito)
        print("Seu saldo atual é de R$ {:.2f}".format(valor))
    if int(option) == 2:
        saque = float(input("Digite o valor que deseja sacar"))
        if valor < saque:
              print("Você não possui saldo para realizar esta operação")
        else:
            valor = valor - saque
            print("Você sacou {:.2f} e seu saldo atual é {:.2f}".format(saque, valor))
            


