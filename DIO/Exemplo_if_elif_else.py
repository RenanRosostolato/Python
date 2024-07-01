import sys

opcao = int (input("informe uma opção: [1] sacar \n [2] Extrato: "))

if opcao == 1:
    valor =float (input("Informe a quantia para o saque:"))
    #...
elif opcao == 2:
    print("Extrato:")

else:
    sys.exit ("Opção Invalida")