def sacar (valor: float):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa")

print("Obrigado por ser nosso cliente, tenha um bom dia")
sacar(100)

def depositar (valor: float):
    saldo = 500
    saldo += valor

    sacar(1000)

#Fique de olho na indentação para não dar problemas com os blocos de códigos.