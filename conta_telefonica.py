minutos = int(input("Digite a quantidade de minutos: "))
if minutos < 200:
	preco = 0.20
elif minutos <= 400:
	preco = 0.28
elif minutos <= 800:
	preco = 0.15
else:
	preco = 0.08

print ("O valor da sua conta telefonica e R$%2.2f" % (minutos * preco) )
