nome = "Guilherme"
idade = 28
profissao = "Programador"  # Corrigido de "Progamador" para "Programador"
linguagem = "Python"
saldo = 45.435

# Corrigindo a ordem dos parâmetros e utilizando o f-string que é mais moderno e legível
print(f"Nome: {nome} Idade: {idade} saldo: {saldo: .2f}")

# Utilizando .format() corretamente e corrigindo a ordem dos parâmetros
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))  # A ordem correta deve ser nome, depois idade

# Demonstrando uso do mesmo argumento múltiplas vezes com .format()
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
