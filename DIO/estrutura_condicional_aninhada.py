conta_normal = False
conta_universitaria = False
saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saldo insuficiente")
    else:
        print("Saque não realizado, saldo insuficiente.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente") 
else:
    print("Saque não realizado. Conta não encontrada. Favor entrar em contato com o seu gerente.")