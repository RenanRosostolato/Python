MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informa a sua idade"))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH") 

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar CNH")
else:
    print("Ainda não pode tirar CNH")



if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Ainda não pode tirar CNH")


#TENDO O ELSE EU NÃO PRECISARIA COLOCAR A LINHA DE CÓDIGO 8, VIRARIA REDUNDÂNCIA.